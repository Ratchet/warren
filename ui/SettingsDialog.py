# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsDialog.ui'
#
# Created: Sat Apr 23 13:37:36 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(400, 338)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        SettingsDialog.setMinimumSize(QtCore.QSize(400, 338))
        SettingsDialog.setMaximumSize(QtCore.QSize(400, 338))
        SettingsDialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        SettingsDialog.setSizeGripEnabled(False)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 300, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtGui.QTabWidget(SettingsDialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.node_settings_tab = QtGui.QWidget()
        self.node_settings_tab.setObjectName("node_settings_tab")
        self.gridLayoutWidget = QtGui.QWidget(self.node_settings_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.node_host_edit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.node_host_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.node_host_edit.setObjectName("node_host_edit")
        self.gridLayout.addWidget(self.node_host_edit, 0, 1, 1, 1)
        self.node_host_label = QtGui.QLabel(self.gridLayoutWidget)
        self.node_host_label.setObjectName("node_host_label")
        self.gridLayout.addWidget(self.node_host_label, 0, 2, 1, 1)
        self.node_port_label = QtGui.QLabel(self.gridLayoutWidget)
        self.node_port_label.setObjectName("node_port_label")
        self.gridLayout.addWidget(self.node_port_label, 1, 2, 1, 1)
        self.node_fcp_port_edit = QtGui.QSpinBox(self.gridLayoutWidget)
        self.node_fcp_port_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.node_fcp_port_edit.setMinimum(1025)
        self.node_fcp_port_edit.setMaximum(65535)
        self.node_fcp_port_edit.setProperty("value", 9481)
        self.node_fcp_port_edit.setObjectName("node_fcp_port_edit")
        self.gridLayout.addWidget(self.node_fcp_port_edit, 1, 1, 1, 1)
        self.testResultsEdit = QtGui.QTextEdit(self.gridLayoutWidget)
        self.testResultsEdit.setObjectName("testResultsEdit")
        self.gridLayout.addWidget(self.testResultsEdit, 2, 1, 1, 1)
        self.testSettingsButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.testSettingsButton.setObjectName("testSettingsButton")
        self.gridLayout.addWidget(self.testSettingsButton, 2, 2, 1, 1)
        self.tabWidget.addTab(self.node_settings_tab, "")
        self.fripe_settings_tab = QtGui.QWidget()
        self.fripe_settings_tab.setObjectName("fripe_settings_tab")
        self.label = QtGui.QLabel(self.fripe_settings_tab)
        self.label.setGeometry(QtCore.QRect(10, 0, 381, 101))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.fripe_settings_tab, "")

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.node_host_edit.setText(QtGui.QApplication.translate("SettingsDialog", "127.0.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.node_host_label.setText(QtGui.QApplication.translate("SettingsDialog", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.node_port_label.setText(QtGui.QApplication.translate("SettingsDialog", "FCP Port", None, QtGui.QApplication.UnicodeUTF8))
        self.testSettingsButton.setText(QtGui.QApplication.translate("SettingsDialog", "Test Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.node_settings_tab), QtGui.QApplication.translate("SettingsDialog", "Node", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsDialog", "Nothing to configure yet", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fripe_settings_tab), QtGui.QApplication.translate("SettingsDialog", "Fripe", None, QtGui.QApplication.UnicodeUTF8))

