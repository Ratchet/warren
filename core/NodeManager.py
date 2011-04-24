from fcp import FCPNode
from PyQt4.QtCore import QThread, SIGNAL, QString

class NodeManager(QThread):

    def __init__(self,config):
        QThread.__init__(self, None)
        self.config = config
        self.node = None
        self.start()

    def run(self):
        print "NodeManager thread starting"
        from time import sleep
        while(True):
            print "NodeManager heartbeat"
            sleep(5)

    def stop(self):
        self.quit()
