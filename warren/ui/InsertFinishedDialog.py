# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/InsertFinishedDialog.ui'
#
# Created: Sun Apr 24 16:37:35 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_InsertFinishedDialog(object):
    def setupUi(self, InsertFinishedDialog):
        InsertFinishedDialog.setObjectName("InsertFinishedDialog")
        InsertFinishedDialog.resize(546, 102)
        self.buttonBox = QtGui.QDialogButtonBox(InsertFinishedDialog)
        self.buttonBox.setGeometry(QtCore.QRect(190, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(InsertFinishedDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 521, 16))
        self.label.setObjectName("label")
        self.keyLineEdit = QtGui.QLineEdit(InsertFinishedDialog)
        self.keyLineEdit.setGeometry(QtCore.QRect(10, 30, 521, 26))
        self.keyLineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.keyLineEdit.setObjectName("keyLineEdit")

        self.retranslateUi(InsertFinishedDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), InsertFinishedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InsertFinishedDialog)

    def retranslateUi(self, InsertFinishedDialog):
        InsertFinishedDialog.setWindowTitle(QtGui.QApplication.translate("InsertFinishedDialog", "Insert Finished", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("InsertFinishedDialog", "The insert has finished. Copy the request key from below:", None, QtGui.QApplication.UnicodeUTF8))

