from fcp import FCPNode
from PyQt4.QtCore import QThread, SIGNAL, QString
import FileManager

class NodeManager(QThread):

    def __init__(self,config):
        QThread.__init__(self, None)
        self.config = config
        self.node = None
        self.standby = True
        self.start()

    def run(self):
        print "NodeManager thread starting"
        QThread.msleep(1000) # wait a second or sometimes signals can't get through right after startup
        self.connectNode()
        self.watchdog = NodeWatchdog(self)
        self.connect(self.watchdog, SIGNAL("nodeNotConnected()"), self.nodeNotConnected)

    def connectNode(self):
        print "Node connection attempt"
        try:
            self.node = FCPNode(name="FripeClient",host=self.config['node']['host'],port=int(self.config['node']['fcp_port']),verbosity=5)
            self.emit(SIGNAL("nodeConnected()"))
        except Exception, e:
            print e
            self.node = None

    def nodeNotConnected(self):
        print "node not connected"
        self.emit(SIGNAL("nodeConnectionLost()"))
        if self.node:
            self.node.shutdown()
            self.node = None
        self.connectNode()

    def pasteCanceled(self):
        if hasattr(self, 'pasteInsert'):
            print "killing insert thread"
            # TODO cancel request in node, too (FCP message "RemoveRequest")
            self.pasteInsert.quit()

    def newPaste(self,qPaste):
        #TODO handle node disconnect during insert
        self.pasteInsert = PutPaste(qPaste, self)
        self.connect(self.pasteInsert, SIGNAL("pasteInsertMessage(QString)"), self.pasteMessageForwarder)
        self.connect(self.pasteInsert, SIGNAL("pasteInsertFinished(QString)"), self.pasteFinished)
        self.pasteInsert.start()

    def pasteFinished(self, result):
        self.emit(SIGNAL("pasteFinished(QString)"),QString(result))
        self.pasteInsert.quit()

    def pasteMessageForwarder(self, msg):
        self.emit(SIGNAL("inserterMessage(QString)"),QString(msg))

    def insertFile(self, url, mimeType):
        print url
        print mimeType
        fileInsert = FileManager.FileInsert(self, url, mimeType, proxy=self.config['proxy']['http'])
        fileInsert.start()

    def stop(self):
        self.watchdog.quit()
        if self.node:
            self.node.shutdown()
        self.quit()

class PutPaste(QThread):
    """ use own thread because we can't send QT signals
        asynchronously from the pyFreenet thread anyway"""

    def __init__(self, paste, parent = None):
        QThread.__init__(self, parent)
        self.paste = paste
        self.nodeManager = parent
        self.node = parent.node

    def run(self):
        keyType = self.nodeManager.config['warren']['pastebin_keytype']
        insert = self.putPaste(self.paste, self.insertcb, async=True, keyType=keyType)
        self.emit(SIGNAL("pasteInsertMessage(QString)"),'Node is inserting text... Please wait')
        insert.wait()

    def putPaste(self, qPaste, callback, async=True, keyType='SSK@'):
        paste = unicode(qPaste)
        paste = paste.encode('utf-8')
        insert = self.node.put(uri=keyType,data=paste,async=async,name='pastebin',Verbosity=5,mimetype="text/plain; charset=utf-8",callback=callback,waituntilsent=True)
        return insert

    # TODO turn these messages in data messages and handle output formating in pastebin dialog
    def insertcb(self,val1,val2):
        if val1=='pending':
            if val2.get('header') == 'URIGenerated':
                text = 'URIGenerated: ' + val2.get('URI') + '\nNode is inserting the key... Please wait.'
                self.emit(SIGNAL("pasteInsertMessage(QString)"),text)
            elif val2.get('header') == 'SimpleProgress':
                text = 'Finalized: ' + val2.get('FinalizedTotal')
                text += ' Total: ' + str(val2.get('Total'))
                text += ' Succeeded: ' + str(val2.get('Succeeded'))
                text += ' Failed: ' + str(val2.get('Failed'))
                text += ' Fatal: ' + str(val2.get('FatallyFailed'))
                text += ' Required: ' + str(val2.get('Required'))
                self.emit(SIGNAL("pasteInsertMessage(QString)"),text)
        elif val1=='failed':
            text = 'ERROR: ' + str(val2.get('CodeDescription','Unknown error'))
            self.emit(SIGNAL("pasteInsertMessage(QString)"),text)
        elif val1=='successful':
            text = 'Successful: ' + val2
            self.emit(SIGNAL("pasteInsertMessage(QString)"),text)
            self.emit(SIGNAL("pasteInsertFinished(QString)"),str(val2))

class NodeWatchdog(QThread):

    def __init__(self,nodeManager):
        QThread.__init__(self, None)
        self.nodeManager = nodeManager
        self.start()

    def run(self):
        QThread.msleep(10000) # on startup wait additional 10 seconds
        while(True):
            QThread.msleep(5000)
            isNodeRunning = self.nodeManager.node is not None and self.nodeManager.node.running
            print "NodeWatchdog heartbeat isnoderunning: ", str(isNodeRunning)
            isNodeAlive = self.nodeManager.node is not None and self.nodeManager.node.nodeIsAlive
            print "NodeWatchdog heartbeat isAlive: ", str(isNodeAlive)
            if not isNodeRunning or not isNodeAlive:
                self.emit(SIGNAL("nodeNotConnected()"))

