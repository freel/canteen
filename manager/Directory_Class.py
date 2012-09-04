# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.Directory_Ui import Ui_Directory
#from ui.DirectoryPage_Ui import Ui_DirectoryPage
from DirectoryPage_Class import DirectoryPage_Class
from localDb_Class import localDb_Class

class Directory_Class(QtGui.QDialog):
    """Окно справочника
    ТУДУ переделать всё к ебеням*осторожно мат, детям не читать*"""
    def __init__(self, table, parent=None):
        self.table = table

        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Directory()
        self.ui.setupUi(self)
        self.connect(self.ui.addRowButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("addRow()"))

        self.insertValsIntoToolBox()

    def addRow(self):
        """Вставляет новую страницу в гармошку
        ТУДУ сделать чтобы пустые вставлял"""
        keys = self.getColNames()
        page = DirectoryPage_Class(self,["" for i in range(len(keys))],keys)
        self.ui.toolBox.insertItem(-1,page,u"Новая запись")

        self.connect(page.ui.saveRowButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("saveRow()"))

    def getColNames(self):
        """Было гдето знач вынести, берет колонок имена"""
        db = localDb_Class()
        db.open_db()
        answer = [tuple[1] for tuple in db.select_col_names(self.table)['rows']]
        db.close_db()
        return answer

    def insertValsIntoToolBox(self):
        """Вставляет значения в страницу"""
        self.selectVals()

    def selectVals(self):
        """Берет данные из базы, вставляет построчно в таблицу на листе"""
        db = localDb_Class()
        db.open_db()
        answer = db.select_all_val(self.table)
        self.rows = answer["rows"]
        self.keys = answer["keys"]
        for i in range(len(self.rows)):
            self.insertValsIntoPages(self.rows[i],self.keys)
        db.close_db()

    def insertValsIntoPages(self,row,key):
        """Вставляет значения в таблицу"""
        page = DirectoryPage_Class(self, row, key)
        self.ui.toolBox.insertItem(-1,page,"%s" % (self.ui.toolBox.count()+1) + " - %s" % row[1])

        self.connect(page.ui.delRowButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("delRow()"))
        self.connect(page.ui.saveRowButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("saveRow()"))

    def saveRow(self):
        """Нечто хитрое, а потом записывает"""
        db = localDb_Class()
        db.open_db()
        strg = [self.ui.toolBox.currentWidget().ui.tableWidget.item(i, 1).text() for i in range(self.ui.toolBox.currentWidget().ui.tableWidget.rowCount())]

        print strg[1:-2]
        answer = db.insert_val(self.table,strg[1:-2])
        db.close_db()

    def delRow(self):
        """Ну тут удаляет"""
        db = localDb_Class()
        db.open_db()
        answer = db.del_row_by_id(self.table,self.ui.toolBox.currentWidget().ui.tableWidget.item(0, 1).text())
        self.ui.toolBox.removeItem(self.ui.toolBox.currentIndex())
        db.close_db()
