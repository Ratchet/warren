from PyQt4.QtGui import QWidget, QLabel, QHBoxLayout, QMenu, qApp, QPixmap
from PyQt4.QtCore import Qt, SIGNAL
from core import Config, NodeManager
from ui import Settings, Pastebin

class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setWindowOpacity(1.0)
        layout = QHBoxLayout()
        layout.setMargin(0)
        self.dropArea = QLabel()
        self.dropArea.setMargin(0)
        self.dropArea.setPixmap(QPixmap('images/dropzone_nocon.png'))

        layout.addWidget(self.dropArea)
        self.setLayout(layout)
        self.setMouseTracking(True)
        self.moving = False

        self.nodeConnected = False

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
        self.nodeConnected = True
        self.dropArea.setPixmap(QPixmap('images/dropzone.png'))

    def nodeNotConnected(self):
        print "mainwindow nodeNotConnected()"
        self.nodeConnected = False
        self.dropArea.setPixmap(QPixmap('images/dropzone_nocon.png'))


    def closeApp(self):
        self.nodeManager.stop()
        qApp.quit()

