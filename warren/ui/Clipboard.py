from PyQt4.QtGui import QWidget, qApp, QClipboard
from PyQt4.QtCore import QString, pyqtSignal
import re

#KEY_PATTERN = re.compile('([USK@|CHK@|SSK@|KSK@].*)[\s|\r|\n]')
#KEY_PATTERN = re.compile('USK@.*|CHK@.*|SSK@.*|KSK@.*?$')
#KEY_PATTERN = re.compile('(USK|SSK)@[a-zA-Z0-9,-\/]*')
#KEY_PATTERN = re.compile("(USK|SSK|CHK|KSK)@([a-zA-Z0-9\,\-\/\~\.]*)")
KEY_PATTERN = re.compile("(USK|SSK|CHK|KSK)@([a-zA-Z0-9\,\-\/\~\.]{50,}\,[A-Z]{4,}[\S]*)")

class Clipboard(QWidget):

    clipboardKey = pyqtSignal(object)

    def __init__(self, parent):
        QWidget.__init__(self, None)

        self.clip = qApp.clipboard()
        self.clip.changed.connect(self.cbChanged)
        self.clip.setText("") # little trick to make clipboard work on windows from the beginning

        if self.clip.supportsSelection():
            self.clip.selectionChanged.connect(self.selChanged)


    def cbChanged(self,event):

        cb = self.clip.mimeData()
        if cb.hasText():
            self.findKeys(unicode(cb.text()).encode('utf-8'))

    def selChanged(self):

        text = unicode(self.clip.text("plain",QClipboard.Selection)).encode('utf-8')
        self.findKeys(text)

    def findKeys(self, text):
        keys = KEY_PATTERN.findall(text)
        if len(keys) > 0:
#            print keys
            self.clipboardKey.emit(keys)
#        textList = text.split(' ')
#        for line in textList:
#            m = KEY_PATTERN.findall(line)
#            if len(m) > 0:
#                self.clipboardKey.emit(m[0].strip())
#                break
            


