from PyQt4.QtGui import QWidget, QLabel, QHBoxLayout, QMenu, qApp, QPixmap
from PyQt4.QtCore import Qt, SIGNAL
from core import Config, NodeManager

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

        self.config = Config.Config()
        self.nodeManager = NodeManager.NodeManager(self.config)
        self.connect(self.nodeManager, SIGNAL("nodeConnected()"), self.nodeConnected)

    def contextMenuEvent(self, event):

        menu = QMenu(self)
        quitAction = menu.addAction("Quit")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            self.closeApp()

    def mouseMoveEvent(self, event):
        if self.moving: self.move(event.globalPos()-self.offset)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = True; self.offset = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = False

    def nodeConnected(self):
        self.dropArea.setPixmap(QPixmap('images/dropzone.png'))

    def closeApp(self):
        self.nodeManager.stop()
        qApp.quit()

