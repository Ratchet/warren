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

    def connectNode(self):
        try:
            self.node = FCPNode(name="FripeClient",host=self.config['node']['host'],port=int(self.config['node']['fcp_port']),verbosity=5)
            self.emit(SIGNAL("nodeConnected()"))
        except Exception, e:
            #TODO show user alert dialog
            print e

    def stop(self):
        self.watchdog.quit()
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
            isNodeRunning = self.nodeManager.node.running
            print "NodeWatchdog heartbeat isnoderunning: ", str(isNodeRunning)
