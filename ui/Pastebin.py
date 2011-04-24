from PyQt4.QtGui import QDialog
from PyQt4 import QtCore
from PastebinDialog import Ui_PastebinDialog

class Pastebin(QDialog):

    def __init__(self):
        QDialog.__init__(self, None)
        self.ui = Ui_PastebinDialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)
#        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)


    def reject(self):
        self.ui.plainTextEdit.clear()
        self.ui.buttonBox.buttons()[0].setEnabled(True)
        self.ui.plainTextEdit.setReadOnly(False)
        self.hide()
