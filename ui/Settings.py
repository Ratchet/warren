from PyQt4.QtGui import QDialog
from SettingsDialog import Ui_SettingsDialog

class Settings(QDialog):

    def __init__(self, config):
        QDialog.__init__(self, None)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.config = config
        print config
        self.populate_fields()

    def populate_fields(self):
        self.ui.node_host_edit.setText(self.config['node']['host'])
        self.ui.node_fcp_port_edit.setProperty("value", self.config['node']['fcp_port'])

    def accept(self):
        #TODO if node change, warn user for reconnect if jobs running, then reconnect node after confirm or cancel
        self.config['node']['host'] = str(self.ui.node_host_edit.text())
        self.config['node']['fcp_port'] = self.ui.node_fcp_port_edit.value()

        self.config.write()
        self.hide()

    def reject(self):
        self.populate_fields()
        self.hide()
