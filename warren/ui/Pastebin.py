from PyQt4.QtGui import QDialog
from PyQt4 import QtCore
from PastebinDialog import Ui_PastebinDialog
from pygments import lexers

class Pastebin(QDialog):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.ui = Ui_PastebinDialog()
        self.ui.setupUi(self)
        self.parent = parent
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        self.buildLexersList()
        self.nodeNotConnected()

    def buildLexersList(self):
        l = lexers.get_all_lexers()
        l = list(l)
        l.sort()

        for idx, lexer in enumerate(l):
            if lexer[1][0] == 'text': textIdx = idx
            self.ui.shl_select.addItem(lexer[0],lexer[1][0])

        self.ui.shl_select.setCurrentIndex(textIdx)

    def accept(self):
        qPaste = QtCore.QString(self.ui.plainTextEdit.document().toPlainText())

        lexIdx = self.ui.shl_select.currentIndex()
        lexer = self.ui.shl_select.itemData(lexIdx)
        lexer = lexer.toString()

        lineNos = self.ui.linenos_checkbox.isChecked()

        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.setReadOnly(True)
        self.ui.buttonBox.buttons()[0].setDisabled(True)
        self.ui.linenos_checkbox.setChecked(False)
        self.ui.plainTextEdit.appendPlainText('Please wait until already running insert is finished.')
        self.emit(QtCore.SIGNAL("newPaste(QString, QString, QString)"),qPaste,lexer,str(lineNos))
        self.hide()

    def reject(self):
        if self.parent.nodeManagerConnected:
            self.ui.plainTextEdit.clear()
            self.ui.linenos_checkbox.setChecked(False)
            self.ui.buttonBox.buttons()[0].setEnabled(True)
            self.ui.plainTextEdit.setReadOnly(False)
        self.hide()

    def nodeNotConnected(self):
        self.ui.buttonBox.buttons()[0].setDisabled(True)
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.appendPlainText('Node not connected. Paste not possible')
        self.ui.plainTextEdit.setReadOnly(True)

    def nodeConnected(self):
        self.ui.plainTextEdit.clear()
        self.ui.buttonBox.buttons()[0].setEnabled(True)
        self.ui.plainTextEdit.setReadOnly(False)






