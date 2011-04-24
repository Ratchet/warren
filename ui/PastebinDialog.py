# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PastebinDialog.ui'
#
# Created: Sun Apr 24 14:45:50 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Pastebin(object):
    def setupUi(self, Pastebin):
        Pastebin.setObjectName("Pastebin")
        Pastebin.resize(500, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Pastebin.sizePolicy().hasHeightForWidth())
        Pastebin.setSizePolicy(sizePolicy)
        Pastebin.setMinimumSize(QtCore.QSize(500, 400))
        Pastebin.setMaximumSize(QtCore.QSize(500, 400))
        Pastebin.setAcceptDrops(False)
        self.plainTextEdit = QtGui.QPlainTextEdit(Pastebin)
        self.plainTextEdit.setGeometry(QtCore.QRect(5, 5, 490, 345))
        self.plainTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtGui.QLabel(Pastebin)
        self.label.setGeometry(QtCore.QRect(10, 360, 271, 25))
        self.label.setObjectName("label")
        self.buttonBox = QtGui.QDialogButtonBox(Pastebin)
        self.buttonBox.setGeometry(QtCore.QRect(320, 360, 173, 25))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Pastebin)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Pastebin.close)
        QtCore.QMetaObject.connectSlotsByName(Pastebin)

    def retranslateUi(self, Pastebin):
        Pastebin.setWindowTitle(QtGui.QApplication.translate("Pastebin", "Pastebin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Pastebin", "Enter text to insert above", None, QtGui.QApplication.UnicodeUTF8))

