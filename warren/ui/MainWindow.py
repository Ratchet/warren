from PyQt4.QtGui import QWidget, QLabel, QHBoxLayout, QMenu, qApp, QPixmap, QFrame, QClipboard, QContextMenuEvent
from PyQt4.QtCore import Qt, SIGNAL
from warren.core import Config, NodeManager, FileManager, Browser
from warren.ui import Settings, Pastebin, DropZone, Clipboard
import sys, os

def determine_path ():
    if os.environ.get('_MEIPASS2'):
        return os.environ['_MEIPASS2']
    else:
        root = __file__
        if os.path.islink (root):
            root = os.path.realpath (root)
        return os.path.dirname (os.path.abspath (root))+'/../images/'

class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(1.0)
        layout = QHBoxLayout()
        layout.setMargin(0)
        self.dropZone = DropZone.DropZone()
        self.dropZone.setMargin(0)
        self.imagePath = determine_path()
        self.dropZone.setPixmap(QPixmap(self.imagePath+'dropzone_nocon.png'))
        # use a little frame until we have nice icons
        self.dropZone.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.dropZone.dropped.connect(self.dropEvent)
        self.dropZone.entered.connect(self.enterEvent)


        layout.addWidget(self.dropZone)
        self.setLayout(layout)
        self.setMouseTracking(True)
        self.moving = False

        self.clipboard = Clipboard.Clipboard(self)
        self.clipboard.clipboardKey.connect(self.clipboardNewKey)
        self.clipboardKeys = list()
        self.clipboardKey = None

        self.nodeManagerConnected = False
        self.dropData = {'accepted' : False, 'url' : None, 'content-type' : None}

        self.config = Config.Config()
        self.settings = Settings.Settings(self.config)
        self.pastebin = Pastebin.Pastebin()
        self.nodeManager = NodeManager.NodeManager(self.config)
        self.setKeepOnTop(self.config['warren'].as_bool('start_on_top'))
        self.connect(self.nodeManager, SIGNAL("nodeConnected()"), self.nodeConnected)
        self.connect(self.nodeManager, SIGNAL("nodeConnectionLost()"), self.nodeNotConnected)
        self.connect(self.nodeManager, SIGNAL("pasteCanceledMessage()"), self.pastebin.reject)
        self.connect(self.pastebin, SIGNAL("newPaste(QString)"), self.nodeManager.newPaste)
        self.connect(self.nodeManager, SIGNAL("pasteFinished()"), self.pastebin.reject)

        self.browser = Browser.Browser(self.config)

    def contextMenuEvent(self, event):

        if self.keepOnTop:
            self.keepOnTopMenuText = "Don't keep icon on top"
        else:
            self.keepOnTopMenuText = 'Keep icon on top'
        menu = QMenu(self)
        pastebinAction = menu.addAction("Pastebin")
        menu.addSeparator()

        if len(self.clipboardKeys)>0:
            downloadMenu = QMenu('Put on download queue', self)
            for idx,key in enumerate(self.clipboardKeys):
                label = key[0]+'@'+key[1][:7]+'...'+key[1][-20:]
                mItem = downloadMenu.addAction(label)
                receiver = lambda taskType=idx:self.dlAction(taskType)
                self.connect(mItem, SIGNAL('triggered()'), receiver)
                downloadMenu.addAction(mItem)
            menu.addMenu(downloadMenu)

            browserMenu = QMenu('Open in Browser', self)
            for idx,key in enumerate(self.clipboardKeys):
                label = key[0]+'@'+key[1][:7]+'...'+key[1][-14:]
                bItem = browserMenu.addAction(label)
                receiver = lambda taskType=idx:self.brAction(taskType)
                self.connect(bItem, SIGNAL('triggered()'), receiver)
                browserMenu.addAction(bItem)
            menu.addMenu(browserMenu)


        menu.addSeparator()
        keepOnTopAction = menu.addAction(self.keepOnTopMenuText)
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
        if action == keepOnTopAction:
            if self.keepOnTop:
                self.setKeepOnTop(False)
            else:
                self.setKeepOnTop(True)

    def setKeepOnTop(self,keepOnTop):
        self.keepOnTop = keepOnTop
        if not keepOnTop:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()


    def dlAction(self,menuIdx):

        key = self.clipboardKeys[menuIdx]

        # put last active key to top of list
        tmp = self.clipboardKeys.pop(menuIdx)
        self.clipboardKeys.insert(0,tmp)
        self.nodeManager.putKeyOnQueue(key[0]+'@'+key[1])

    def brAction(self,menuIdx):

        key = self.clipboardKeys[menuIdx]

        # put last active key to top of list
        tmp = self.clipboardKeys.pop(menuIdx)
        self.clipboardKeys.insert(0,tmp)
        self.browser.openKeyInBrowser(key[0]+'@'+key[1])


    def clipboardNewKey(self,keys):
        for key in keys:
            if key not in self.clipboardKeys:
                if len(self.clipboardKeys) >= self.config['warren']['max_clipboard_keys']:
                    self.clipboardKeys.pop(-1)
                self.clipboardKeys.insert(0,key)

    def enterEvent(self, mimeData = None):

        if not mimeData or not hasattr(mimeData, 'formats'): return

        if self.nodeManagerConnected:

            self.dropZone.setPixmap(QPixmap(self.imagePath+'dropzone_analyze.png'))
            fileinfo = FileManager.checkFileForInsert(mimeData, proxy=self.config['proxy']['http']) # TODO: this is still blocking

            if fileinfo:
                self.dropZone.setPixmap(QPixmap(self.imagePath+'dropzone_ok.png'))
                self.dropData['accepted'] = True
                self.dropData['url'] = fileinfo[0]
                self.dropData['content-type'] = fileinfo[1]
            else:
                self.dropZone.setPixmap(QPixmap(self.imagePath+'dropzone_rejected.png'))

    def dropEvent(self, mimeData = None):

        if not mimeData or not hasattr(mimeData, 'formats') or not self.nodeManagerConnected:
            self.dropZone.setPixmap(QPixmap(self.imagePath+'dropzone.png')) # because it's leave event, too (mimeData=None)
            self.dropData = {'accepted' : False, 'url' : None, 'content-type' : None}
            return

        if self.dropData['accepted']:
            self.nodeManager.insertFile(self.dropData['url'], self.dropData['content-type'])

        self.dropZone.setPixmap(QPixmap(self.imagePath+'dropzone.png'))

    def mouseMoveEvent(self, event):
        if self.moving: self.move(event.globalPos()-self.offset)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = True; self.offset = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = False

    def nodeConnected(self):
        self.nodeManagerConnected = True
        self.dropZone.setPixmap(QPixmap(self.imagePath+'dropzone.png'))

    def nodeNotConnected(self):
        self.nodeManagerConnected = False
        self.dropZone.setPixmap(QPixmap(self.imagePath+'dropzone_nocon.png'))


    def closeApp(self):
        self.nodeManager.stop()
        qApp.quit()

