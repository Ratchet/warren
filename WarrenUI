#!/usr/bin/env python2

from PyQt4.QtGui import QApplication
from warren.ui.MainWindow import MainWindow
import sys

def start():
    app = QApplication(sys.argv)
    app.setApplicationName('Warren')
    app.setQuitOnLastWindowClosed(True)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    start()
