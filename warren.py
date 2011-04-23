from PyQt4.QtGui import QApplication
from ui.MainWindow import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Warren')
    app.setQuitOnLastWindowClosed(True)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
