from PyQt4.QtGui import QWidget, QLabel, QHBoxLayout, QMenu, qApp, QPixmap
from PyQt4.QtCore import Qt, SIGNAL
from core import Config, NodeManager, FileManager
from ui import Settings, Pastebin, DropZone

class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        #TODO "keep on top" window option
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setWindowOpacity(1.0)
        layout = QHBoxLayout()
        layout.setMargin(0)
        self.dropZone = DropZone.DropZone()
        self.dropZone.setMargin(0)
        self.dropZone.setPixmap(QPixmap('images/dropzone_nocon.png'))
        self.dropZone.dropped.connect(self.dropEvent)
        self.dropZone.entered.connect(self.enterEvent)

        layout.addWidget(self.dropZone)
        self.setLayout(layout)
        self.setMouseTracking(True)
        self.moving = False

        self.nodeManagerConnected = False
        self.dropData = {'accepted' : False, 'url' : None, 'content-type' : None}

        self.config = Config.Config()
        self.settings = Settings.Settings(self.config)
        self.pastebin = Pastebin.Pastebin()
        self.nodeManager = NodeManager.NodeManager(self.config)
        self.connect(self.nodeManager, SIGNAL("nodeConnected()"), self.nodeConnected)
        self.connect(self.nodeManager, SIGNAL("nodeConnectionLost()"), self.nodeNotConnected)
        self.connect(self.pastebin, SIGNAL("newPaste(QString)"), self.nodeManager.newPaste)
        self.connect(self.pastebin, SIGNAL("pasteCanceled()"), self.nodeManager.pasteCanceled)
        self.connect(self.nodeManager, SIGNAL("inserterMessage(QString)"), self.pastebin.inserterMessage)
        self.connect(self.nodeManager, SIGNAL("pasteFinished(QString)"), self.pastebin.pasteFinished)

    def contextMenuEvent(self, event):

        menu = QMenu(self)
        pastebinAction = menu.addAction("Pastebin")
        settingsAction = menu.addAction("Settings")
        menu.addSeparator()
        quitAction = menu.addAction("Quit")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            self.closeApp()
        if action == settingsAction:
            self.settings.show()
        if action == pastebinAction:
            self.pastebin.show()

    def enterEvent(self, mimeData = None):
        print "enter event mainwindow"
        if not mimeData or not hasattr(mimeData, 'formats'): return
        if self.nodeManagerConnected:
            fileinfo = FileManager.checkFileForInsert(mimeData)
            #TODO show a dropzone_rejected.png if checkFileForInsert() returns False
            if fileinfo:
                self.dropZone.setPixmap(QPixmap('images/dropzone_ok.png'))
                self.dropData['accepted'] = True
                self.dropData['url'] = fileinfo[0]
                self.dropData['content-type'] = fileinfo[1]

    def dropEvent(self, mimeData = None):
        print "drop event mainwindow"
        if not mimeData or not hasattr(mimeData, 'formats') or not self.nodeManagerConnected:
            self.dropZone.setPixmap(QPixmap('images/dropzone.png')) # because it's leave event, too
            self.dropData = {'accepted' : False, 'url' : None, 'content-type' : None}
            return
        # TODO do the insert start here
        if self.dropData['accepted']:
            print "starting file insert: %s %s" % (self.dropData['url'], self.dropData['content-type'])
        self.dropZone.setPixmap(QPixmap('images/dropzone.png'))

    def mouseMoveEvent(self, event):
        if self.moving: self.move(event.globalPos()-self.offset)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = True; self.offset = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = False

    def nodeConnected(self):
        print "mainwindow nodeConnected()"
        self.nodeManagerConnected = True
        self.dropZone.setPixmap(QPixmap('images/dropzone.png'))

    def nodeNotConnected(self):
        print "mainwindow nodeNotConnected()"
        self.nodeManagerConnected = False
        self.dropZone.setPixmap(QPixmap('images/dropzone_nocon.png'))


    def closeApp(self):
        self.nodeManager.stop()
        qApp.quit()

