# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warren/ui/PasteInsert.ui'
#
# Created: Tue May 10 18:24:47 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PasteInsertDialog(object):
    def setupUi(self, PasteInsertDialog):
        PasteInsertDialog.setObjectName("PasteInsertDialog")
        PasteInsertDialog.resize(546, 106)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PasteInsertDialog.sizePolicy().hasHeightForWidth())
        PasteInsertDialog.setSizePolicy(sizePolicy)
        PasteInsertDialog.setMaximumSize(QtCore.QSize(546, 106))
        self.buttonBox = QtGui.QDialogButtonBox(PasteInsertDialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 70, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.keyLineEdit = QtGui.QLineEdit(PasteInsertDialog)
        self.keyLineEdit.setGeometry(QtCore.QRect(10, 40, 521, 26))
        self.keyLineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.progressBar = QtGui.QProgressBar(PasteInsertDialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 521, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtGui.QPushButton(PasteInsertDialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 171, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(PasteInsertDialog)
        QtCore.QMetaObject.connectSlotsByName(PasteInsertDialog)

    def retranslateUi(self, PasteInsertDialog):
        PasteInsertDialog.setWindowTitle(QtGui.QApplication.translate("PasteInsertDialog", "Inserting Pastebin", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("PasteInsertDialog", "Copy key to clipboard", None, QtGui.QApplication.UnicodeUTF8))

