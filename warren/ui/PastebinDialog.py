# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warren/ui/PastebinDialog.ui'
#
# Created: Wed May  4 21:42:41 2011
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
        PastebinDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        PastebinDialog.setAcceptDrops(False)
        self.verticalLayout = QtGui.QVBoxLayout(PastebinDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(PastebinDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtGui.QPlainTextEdit(PastebinDialog)
        self.plainTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.buttonBox = QtGui.QDialogButtonBox(PastebinDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PastebinDialog)
        QtCore.QMetaObject.connectSlotsByName(PastebinDialog)

    def retranslateUi(self, PastebinDialog):
        PastebinDialog.setWindowTitle(QtGui.QApplication.translate("PastebinDialog", "Pastebin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PastebinDialog", "Enter text to insert below", None, QtGui.QApplication.UnicodeUTF8))

