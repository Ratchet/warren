# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warren/ui/PasteInsert.ui'
#
# Created: Thu Apr 28 19:01:43 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_InsertFinishedDialog(object):
    def setupUi(self, InsertFinishedDialog):
        InsertFinishedDialog.setObjectName("InsertFinishedDialog")
        InsertFinishedDialog.resize(546, 106)
        self.buttonBox = QtGui.QDialogButtonBox(InsertFinishedDialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 70, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.keyLineEdit = QtGui.QLineEdit(InsertFinishedDialog)
        self.keyLineEdit.setGeometry(QtCore.QRect(10, 40, 521, 26))
        self.keyLineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.progressBar = QtGui.QProgressBar(InsertFinishedDialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 521, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtGui.QPushButton(InsertFinishedDialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 171, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(InsertFinishedDialog)
        QtCore.QMetaObject.connectSlotsByName(InsertFinishedDialog)

    def retranslateUi(self, InsertFinishedDialog):
        InsertFinishedDialog.setWindowTitle(QtGui.QApplication.translate("InsertFinishedDialog", "Insert Finished", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("InsertFinishedDialog", "Copy key to clipboard", None, QtGui.QApplication.UnicodeUTF8))

