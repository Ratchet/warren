# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warren/ui/FileSent.ui'
#
# Created: Thu Apr 28 18:58:02 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_fileDroppedDialog(object):
    def setupUi(self, fileDroppedDialog):
        fileDroppedDialog.setObjectName("fileDroppedDialog")
        fileDroppedDialog.resize(378, 151)
        self.buttonBox = QtGui.QDialogButtonBox(fileDroppedDialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 100, 71, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(fileDroppedDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 371, 81))
        self.label.setObjectName("label")
        self.checkBox = QtGui.QCheckBox(fileDroppedDialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 100, 271, 31))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(fileDroppedDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), fileDroppedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(fileDroppedDialog)

    def retranslateUi(self, fileDroppedDialog):
        fileDroppedDialog.setWindowTitle(QtGui.QApplication.translate("fileDroppedDialog", "File sent", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("fileDroppedDialog", "Warren sends the file to your freenet node now.\n"
"\n"
"Visit your node\'s Upload page to see the progress\n"
"of the insert and to change priorities.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("fileDroppedDialog", "Don\'t show this message again.", None, QtGui.QApplication.UnicodeUTF8))

