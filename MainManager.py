# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from manager.MainWindowManager_Class import MainWindow_Class

if __name__ == "__main__":
    """Запуск основного приложения"""
    app = QtGui.QApplication(sys.argv)

    win = MainWindow_Class(None)
    win.show()
    sys.exit(app.exec_())