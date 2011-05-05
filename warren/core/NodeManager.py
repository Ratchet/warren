from fcp import FCPNode
from PyQt4.QtCore import QThread, SIGNAL, QString, pyqtSignal
from PyQt4.QtGui import QDialog, QClipboard, qApp
from warren.ui.FileSent import Ui_fileDroppedDialog
from warren.ui.PasteInsert import Ui_PasteInsertDialog
import FileManager
import os.path

SECLEVELS = {'LOW':0, 'NORMAL':1, 'HIGH':2, 'MAXIMUM':3}

class NodeManager(QThread):

    pasteCanceledMessage = pyqtSignal()

    def __init__(self,config):
        QThread.__init__(self, None)
        self.config = config
        self.node = None
        self.standby = True
        self.physicalSeclevel = None
        self.nodeDownloadDir = None
        self.downloadDDA = False
        self.start()

    def run(self):
        QThread.msleep(1000) # wait a second or sometimes signals can't get through right after startup
        self.connectNode()
        self.watchdog = NodeWatchdog(self)
        self.connect(self.watchdog, SIGNAL("nodeNotConnected()"), self.nodeNotConnected)

    def connectNode(self):
        try:
            self.node = FCPNode(name="WarrenClient",host=self.config['node']['host'],port=int(self.config['node']['fcp_port']),verbosity=0)
            self.updateNodeConfigValues()
            self.emit(SIGNAL("nodeConnected()"))
        except Exception, e:
            self.node = None

    def updateNodeConfigValues(self):
        nconfig = self.node.getconfig(async=False,WithCurrent=True,WithExpertFlag=True)
        self.physicalSeclevel = SECLEVELS[nconfig['current.security-levels.physicalThreatLevel']]
        self.nodeDownloadDir = nconfig['current.node.downloadsDir']
        self.downloadDDA = nconfig['expertFlag.fcp.assumeDownloadDDAIsAllowed']=='true'
        if not os.path.isabs(self.nodeDownloadDir):
            self.nodeDownloadDir = os.path.join(nconfig['current.node.cfgDir'], self.nodeDownloadDir)

    def nodeNotConnected(self):
        self.emit(SIGNAL("nodeConnectionLost()"))
        if self.node:
            self.node.shutdown()
            self.node = None
        self.connectNode()

    def putKeyOnQueue(self, key):
        if self.physicalSeclevel > 0:
            testDDAResult = False
        else:
            if self.downloadDDA:
                testDDAResult = True
            else:
                testDDAResult = False
                try:
                    testDDA = self.node.testDDA(async=False, Directory=self.nodeDownloadDir, WantWriteDirectory=True, timeout=5)

                    if 'TestDDAComplete' in str(testDDA.items()) and "'WriteDirectoryAllowed', 'true'" in str(testDDA.items()): #TODO check for the real keys
                        testDDAResult = True
                except Exception, e:
                    testDDAResult = False

        if testDDAResult:
            filename = os.path.join(self.nodeDownloadDir, key.split('/')[-1])
            self.node.get(key,async=True, Global=True, persistence='forever',priority=4, id='Warren:'+key.split('/')[-1], file=filename)
        else:
            self.node.get(key,async=True, Global=True, persistence='forever',priority=4, id='Warren:'+key.split('/')[-1])



    def pasteCanceled(self):
        if hasattr(self, 'pasteInsert'):
            # TODO cancel request in node, too (FCP message "RemoveRequest")
            self.pasteCanceledMessage.emit()
            self.pasteInsertDialog.close()

    def newPaste(self,qPaste):
        #TODO handle node disconnect during insert

        self.pasteInsertDialog = PasteInsert()
        self.pasteInsertDialog.show()

        self.pasteInsert = PutPaste(qPaste, self)
        self.pasteInsert.message.connect(self.pasteInsertDialog.messageReceived)

        self.pasteInsertDialog.ui.buttonBox.rejected.connect(self.pasteCanceled)

        self.pasteInsert.start()


    def pasteMessageForwarder(self, msg):
        self.emit(SIGNAL("inserterMessage(QString)"),QString(msg))

    def insertFile(self, url, mimeType):
        fileInsert = FileManager.FileInsert(self, url, mimeType, proxy=self.config['proxy']['http'])
        fileInsert.start()
        showTip = self.config['warren'].as_bool('show_file_dropped_dialog')
        if showTip:
            self.dropped = FileDropped(self)
            self.dropped.show()

    def stop(self):
        self.watchdog.quit()
        if self.node:
            self.node.shutdown()
        self.quit()

class PasteInsert(QDialog):

    pasteFinished = pyqtSignal()

    def __init__(self):
        QDialog.__init__(self, None)
        self.ui = Ui_PasteInsertDialog()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)
        self.ui.pushButton.setDisabled(True)
        self.ui.keyLineEdit.setReadOnly(True)
        self.ui.keyLineEdit.setText('Key not yet generated... Please wait.')
        self.ui.buttonBox.buttons()[0].setDisabled(True)
        self.ui.pushButton.pressed.connect(self.pasteClipCopy)
        self.key = None

    def pasteClipCopy(self):
        clip = qApp.clipboard()
        clip.setText(str(self.key))
        if clip.supportsSelection():
            clip.setText(str(self.key),QClipboard.Selection)


    def messageReceived(self,msg):
        val1 = msg[0]
        val2 = msg[1]
        if val1=='pending':
            if val2.get('header') == 'URIGenerated':
                self.ui.keyLineEdit.setText(val2.get('URI'))
                self.ui.keyLineEdit.setCursorPosition(0)
                self.ui.pushButton.setEnabled(True)
                self.key = val2.get('URI')
            elif val2.get('header') == 'SimpleProgress':
                self.ui.progressBar.setMaximum(val2.get('Total'))
                self.ui.progressBar.setValue(val2.get('Succeeded'))
        elif val1=='failed':
            self.ui.keyLineEdit.setText('Insert Failed: '+ str(val2.get('CodeDescription','Unknown error')))
        elif val1=='successful':
            self.ui.buttonBox.buttons()[0].setEnabled(True)
            self.ui.buttonBox.buttons()[1].setEnabled(False)
            self.ui.keyLineEdit.setCursorPosition(0)
            self.pasteFinished.emit()



class FileDropped(QDialog):

    def __init__(self, nodeManager):
        QDialog.__init__(self, None)
        self.config = nodeManager.config
        self.ui = Ui_fileDroppedDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)

    def accept(self):
        if self.ui.checkBox.isChecked():
            self.config['warren']['show_file_dropped_dialog']=False
            self.config.write()
        self.close()

    def reject(self):
        self.hide()
        self.close()

class PutPaste(QThread):
    """ use own thread because we can't send QT signals
        asynchronously from the pyFreenet thread anyway"""

    message = pyqtSignal(object)

    def __init__(self, paste, parent = None):
        QThread.__init__(self, parent)
        self.paste = paste
        self.nodeManager = parent
        self.node = parent.node

    def run(self):
        keyType = self.nodeManager.config['warren']['pastebin_keytype']
        insert = self.putPaste(self.paste, self.insertcb, async=True, keyType=keyType)
        insert.wait()

    def putPaste(self, qPaste, callback, async=True, keyType='SSK@'):
        paste = unicode(qPaste)
        paste = paste.encode('utf-8')
        insert = self.node.put(uri=keyType,data=paste,async=async,name='pastebin',Verbosity=5,mimetype="text/plain; charset=utf-8",callback=callback,waituntilsent=True,priority=2,realtime=True)
        return insert

    def insertcb(self,val1,val2):
        self.message.emit([val1,val2])

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
            isNodeAlive = self.nodeManager.node is not None and self.nodeManager.node.nodeIsAlive
            if not isNodeRunning or not isNodeAlive:
                self.emit(SIGNAL("nodeNotConnected()"))

