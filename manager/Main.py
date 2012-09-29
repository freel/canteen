# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from MainWindow_Class import MainWindow_Class

from localDb_Class import localDb_Class
from ui.BaseChoice_Ui import Ui_BaseChoice

class Base(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_BaseChoice()
        self.ui.setupUi(self)
        
        self.connect(self.ui.commandLinkButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("nextwin()"))
        
        db = localDb_Class()
        bases = db.select_all_val('base')['rows']
        db.close_db()
        
        self.b = []
        for b in bases:
            self.b.append(b)
            self.ui.comboBox.addItem(b['name'])
        
        
    def nextwin(self):
        base = self.b[self.ui.comboBox.currentIndex()]['id']
        self.close()
        MainWindow(base)

def MainWindow(base):
    win = MainWindow_Class(None,base)
    win.show()

if __name__ == "__main__":
    """Запуск основного приложения"""
    app = QtGui.QApplication(sys.argv)

    win = Base()
    win.show()
    sys.exit(app.exec_())
