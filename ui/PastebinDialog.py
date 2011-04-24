# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PastebinDialog.ui'
#
# Created: Sun Apr 24 14:57:22 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PastebinDialog(object):
    def setupUi(self, PastebinDialog):
        PastebinDialog.setObjectName("PastebinDialog")
        PastebinDialog.resize(500, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PastebinDialog.sizePolicy().hasHeightForWidth())
        PastebinDialog.setSizePolicy(sizePolicy)
        PastebinDialog.setMinimumSize(QtCore.QSize(500, 400))
        PastebinDialog.setMaximumSize(QtCore.QSize(500, 400))
        PastebinDialog.setAcceptDrops(False)
        self.plainTextEdit = QtGui.QPlainTextEdit(PastebinDialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(5, 5, 490, 345))
        self.plainTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtGui.QLabel(PastebinDialog)
        self.label.setGeometry(QtCore.QRect(10, 360, 271, 25))
        self.label.setObjectName("label")
        self.buttonBox = QtGui.QDialogButtonBox(PastebinDialog)
        self.buttonBox.setGeometry(QtCore.QRect(320, 360, 173, 25))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(PastebinDialog)
        QtCore.QMetaObject.connectSlotsByName(PastebinDialog)

    def retranslateUi(self, PastebinDialog):
        PastebinDialog.setWindowTitle(QtGui.QApplication.translate("PastebinDialog", "Pastebin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PastebinDialog", "Enter text to insert above", None, QtGui.QApplication.UnicodeUTF8))

