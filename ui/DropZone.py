from PyQt4 import QtCore, QtGui


class DropZone(QtGui.QLabel):

    changed = QtCore.pyqtSignal(QtCore.QMimeData)
    entered = QtCore.pyqtSignal(QtCore.QMimeData)

    def __init__(self, parent = None):
        super(DropZone, self).__init__(parent)
        self.setMinimumSize(70, 70)
        self.setMaximumSize(70, 70)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        self.clear()

    def dragEnterEvent(self, event):
        print "drag enter"
        self.entered.emit(event.mimeData())
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        self.changed.emit(event.mimeData())
        return

    def dragLeaveEvent(self, event):
        self.clear()
        event.accept()

    def clear(self):
        self.changed.emit(None)


