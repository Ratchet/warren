from PyQt4.QtGui import QDialog
from SettingsDialog import Ui_SettingsDialog

class Settings(QDialog):

    def __init__(self, config):
        QDialog.__init__(self, None)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        # TODO fcp test node client
        self.ui.testResultsEdit.append('Settings test not yet implemented')

        self.ui.testResultsEdit.setReadOnly(True)
        self.ui.testSettingsButton.setDisabled(True)
        self.ui.file_key_type_box.addItem('SSK@')
        self.ui.file_key_type_box.addItem('CHK@')
        self.ui.pastebin_key_type_box.addItem('SSK@')
        self.ui.pastebin_key_type_box.addItem('CHK@')
        self.config = config
        self.populate_fields()

    def populate_fields(self):
        self.ui.node_host_edit.setText(self.config['node']['host'])
        self.ui.node_fcp_port_edit.setProperty("value", self.config['node']['fcp_port'])
        self.ui.node_http_port_edit.setProperty("value", self.config['node']['fproxy_port'])
        self.ui.proxy_host_edit.setText(self.config['proxy']['http']['host'])
        self.ui.proxy_port_edit.setProperty("value", self.config['proxy']['http']['port'])
        self.ui.browser_command.setText(self.config['warren']['browser_command'])
        self.ui.max_clipboard_keys.setProperty("value", self.config['warren']['max_clipboard_keys'])
        if self.config['warren']['pastebin_keytype']=='SSK@':
            pbk = 0
        else:
            pbk = 1
        if self.config['warren']['file_keytype']=='SSK@':
            fk = 0
        else:
            fk = 1
        self.ui.pastebin_key_type_box.setCurrentIndex(pbk)
        self.ui.file_key_type_box.setCurrentIndex(fk)

    def accept(self):
        #TODO if node change, warn user for reconnect if jobs running, then reconnect node after confirm or cancel
        self.config['node']['host'] = str(self.ui.node_host_edit.text())
        self.config['node']['fcp_port'] = self.ui.node_fcp_port_edit.value()
        self.config['node']['fproxy_port'] = self.ui.node_http_port_edit.value()
        self.config['proxy']['http']['host'] = str(self.ui.proxy_host_edit.text())
        self.config['proxy']['http']['port'] = self.ui.proxy_port_edit.value()
        self.config['warren']['pastebin_keytype'] = self.ui.pastebin_key_type_box.currentIndex() == 0 and 'SSK@' or 'CHK@'
        self.config['warren']['file_keytype'] = self.ui.file_key_type_box.currentIndex() == 0 and 'SSK@' or 'CHK@'
        self.config['warren']['browser_command'] = str(self.ui.browser_command.text())
        self.config['warren']['max_clipboard_keys'] = self.ui.max_clipboard_keys.value()

        self.config.write()
        self.hide()

    def reject(self):
        self.populate_fields()
        self.hide()
