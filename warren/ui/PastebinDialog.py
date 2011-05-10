# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warren/ui/PastebinDialog.ui'
#
# Created: Tue May 10 22:04:56 2011
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
        self.gridLayout = QtGui.QGridLayout(PastebinDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(PastebinDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.plainTextEdit = QtGui.QPlainTextEdit(PastebinDialog)
        self.plainTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 3)
        self.shl_select = QtGui.QComboBox(PastebinDialog)
        self.shl_select.setObjectName("shl_select")
        self.gridLayout.addWidget(self.shl_select, 2, 0, 1, 1)
        self.linenos_checkbox = QtGui.QCheckBox(PastebinDialog)
        self.linenos_checkbox.setObjectName("linenos_checkbox")
        self.gridLayout.addWidget(self.linenos_checkbox, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PastebinDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 1)

        self.retranslateUi(PastebinDialog)
        QtCore.QMetaObject.connectSlotsByName(PastebinDialog)

    def retranslateUi(self, PastebinDialog):
        PastebinDialog.setWindowTitle(QtGui.QApplication.translate("PastebinDialog", "Pastebin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PastebinDialog", "Enter text to insert below", None, QtGui.QApplication.UnicodeUTF8))
        self.linenos_checkbox.setText(QtGui.QApplication.translate("PastebinDialog", "Add line numbers", None, QtGui.QApplication.UnicodeUTF8))

