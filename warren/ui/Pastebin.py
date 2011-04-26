from PyQt4.QtGui import QDialog
from PyQt4 import QtCore
from PastebinDialog import Ui_PastebinDialog
from InsertFinishedDialog import Ui_InsertFinishedDialog

class Pastebin(QDialog):

    def __init__(self):
        QDialog.__init__(self, None)
        self.ui = Ui_PastebinDialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)

    def accept(self):
        qPaste = QtCore.QString(self.ui.plainTextEdit.document().toPlainText())
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.setReadOnly(True)
        self.ui.buttonBox.buttons()[0].setDisabled(True)
        self.ui.plainTextEdit.appendPlainText('Sending text to Node... Please wait.')
        self.emit(QtCore.SIGNAL("newPaste(QString)"),qPaste)

    def reject(self):
        self.ui.plainTextEdit.clear()
        self.ui.buttonBox.buttons()[0].setEnabled(True)
        self.ui.plainTextEdit.setReadOnly(False)
        self.emit(QtCore.SIGNAL("pasteCanceled()"))
        self.hide()

    def pasteFinished(self, result):
        if_dialog = InsertFinished(self,result)
        if_dialog.show()
        self.ui.plainTextEdit.clear()
        self.ui.buttonBox.buttons()[0].setEnabled(True)
        self.ui.plainTextEdit.setReadOnly(False)
        self.hide()


    def inserterMessage(self, msg):
        self.ui.plainTextEdit.appendPlainText(msg)




class InsertFinished(QDialog):

    def __init__(self, parent, key):
        QDialog.__init__(self, parent)
        self.ui = Ui_InsertFinishedDialog()
        self.ui.setupUi(self)
        self.ui.keyLineEdit.setText(key)
        self.ui.keyLineEdit.setReadOnly(True)
        self.ui.keyLineEdit.setCursorPosition(0)

    def reject(self):
        self.hide()
        self.close()
