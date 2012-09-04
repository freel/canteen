# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.Storage_Ui import Ui_Storage
from localDb_Class import localDb_Class
from Shift_Class import Shift
from Income_Class import Income_Class
from Compare_Class import IncomeFrom1C_Class

class Storage_Class(QtGui.QDialog):
    """Склад"""
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Storage()
        self.ui.setupUi(self)
        self.parent = parent

        self.fillStorage()
        self.ui.tableStorageWidget.setCurrentCell(0,0)

        self.connect(self.ui.addIncomeButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_addIncomeButton()"))
        self.connect(self.ui.delIncomeButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_delIncomeButton()"))
        self.connect(self.ui.importFrom1CButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_importFrom1CButton()"))

    def renew(self):
        #self.ui.tableStorageWidget.clear()
        for i in range(self.ui.tableStorageWidget.rowCount()):
            self.ui.tableStorageWidget.removeRow(0)
        self.fillStorage()

    def on_click_addIncomeButton(self):
        """Открывает приход"""
        form = Income_Class(self)
        form.show()

    def on_click_delIncomeButton(self):
        """Удаляет выделенную запись

        СДЕЛАТЬ ПРОВЕРКУ НА ССЫЛКИ ИЗ БАЗЫ
        """
        rownum = self.ui.tableStorageWidget.currentRow()
        id_to_del = int(self.ui.tableStorageWidget.item(rownum,0).text())
        if not self.check_refs(id_to_del):
            db = localDb_Class()
            #db.del_row_by_id('income',id_to_del)
            db.close_db()
            self.renew()
        else:
            print "blablabla"

    def on_click_importFrom1CButton(self):
        form = IncomeFrom1C_Class(self)
        form.show()

    def check_refs(self,id_to_del):
        """Проверяет есть ли в базе ссылки на этот"""
        db = localDb_Class()
        answer = db.select_val_by_col('calculate','income',"%s" % id_to_del)
        db.close_db()
        print answer['rows']
        try:
            return answer['rows'][0]
        except:
            return False

    def fillStorage(self):
        """Заполняет склад из базы
        TODO сделать по человечьи(вместо циферок значения из справочников поставить)"""
        for row in self.select_incomes():
            print row
            itemNumber = self.ui.tableStorageWidget.rowCount()
            self.ui.tableStorageWidget.setRowCount(itemNumber +1)
            for col in range(len(row)):
                item = QtGui.QTableWidgetItem()
                self.ui.tableStorageWidget.setItem(itemNumber, col, item)
                self.ui.tableStorageWidget.item(itemNumber, col).setText("%s" % row[col])

    def select_incomes(self):
        """Выбирает все необходимые значения из базы"""
        db = localDb_Class()
        query = "SELECT i.id, i.name, m.name, i.count, i.rest, i.price, p.for_sale, i.date FROM income as i, measure as m, product as p WHERE "
        query += "i.active<>0 AND m.code = i.measure AND p.id = i.product"
        incom = db.exec_query(query)['rows']
        db.close_db()
        print incom
        return incom