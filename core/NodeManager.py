from fcp import FCPNode
from PyQt4.QtCore import QThread, SIGNAL, QString

class NodeManager(QThread):

    def __init__(self,config):
        QThread.__init__(self, None)
        self.config = config
        self.node = None
        self.standby = True
        self.start()

    def run(self):
        print "NodeManager thread starting"
        self.connectNode()
        self.watchdog = NodeWatchdog(self)
        self.connect(self.watchdog, SIGNAL("nodeNotConnected()"), self.nodeNotConnected)

    def connectNode(self):
        print "Node connection attempt"
        try:
            self.node = FCPNode(name="FripeClient",host=self.config['node']['host'],port=int(self.config['node']['fcp_port']),verbosity=5)
            self.emit(SIGNAL("nodeConnected()"))
        except Exception, e:
            #TODO show user alert dialog
            print e
            self.node = None

    def nodeNotConnected(self):
        print "not not connected"
        self.emit(SIGNAL("nodeConnectionLost()"))
        if self.node:
            self.node.shutdown()
            self.node = None
        self.connectNode()

    def stop(self):
        self.watchdog.quit()
        if self.node:
            self.node.shutdown()
        self.quit()

class NodeWatchdog(QThread):

    def __init__(self,nodeManager):
        QThread.__init__(self, None)
        self.nodeManager = nodeManager
        self.start()

    def run(self):
        while(True):
            QThread.msleep(5000)
            isNodeRunning = self.nodeManager.node is not None and self.nodeManager.node.running
            print "NodeWatchdog heartbeat isnoderunning: ", str(isNodeRunning)
            isNodeAlive = self.nodeManager.node is not None and self.nodeManager.node.nodeIsAlive
            print "NodeWatchdog heartbeat isAlive: ", str(isNodeAlive)
            if not isNodeRunning or not isNodeAlive:
                self.emit(SIGNAL("nodeNotConnected()"))

