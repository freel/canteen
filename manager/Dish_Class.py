# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.Dish_Ui import Ui_Dish
from localDb_Class import localDb_Class
from Product_Class import Product_Class
from datetime import datetime

class Dish_Class(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dish()
        self.ui.setupUi(self)
        self.parent = parent

        self.box = {}
        self.percent = {}
        self.compliteForm()


        self.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("saveData()"))
        self.connect(self.ui.addProductButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("addProduct()"))
        self.connect(self.ui.consumptionTableWidget, QtCore.SIGNAL("currentCellChanged(int, int, int, int)"), QtCore.SLOT("checkProduct(int, int, int, int)"))

    def compliteForm(self):
        self.compliteSectionBox()
        #self.compliteProductBox()

    def compliteSectionBox(self):
        for section in self.getSections():
            self.ui.sectionBox.addItem(section['name'])

    def compliteProductBox(self, box):
        for product in self.getProducts():
            box.addItem(product[1])
        box.setCurrentIndex(-1)

    def addProduct(self):
        itemNumber = self.ui.consumptionTableWidget.rowCount()
        self.ui.consumptionTableWidget.setRowCount(itemNumber +1)
        self.box[itemNumber] = QtGui.QComboBox()
        self.box[itemNumber].setEditable(True)
        self.compliteProductBox(self.box[itemNumber])
        item = QtGui.QTableWidgetItem()
        self.ui.consumptionTableWidget.setItem(self.ui.consumptionTableWidget.rowCount() - 1, 1, item)
        self.ui.consumptionTableWidget.setCellWidget(self.ui.consumptionTableWidget.rowCount() - 1, 0, self.box[itemNumber])

    def checkProduct(self, row, cell, prow, pcell):
        if pcell==0:
            try:
                db = localDb_Class()
                query = "SELECT c.percent FROM coefficient as c, product as p WHERE p.id = c.product AND p.name='%s'" % self.ui.consumptionTableWidget.cellWidget(row, 0).currentText()
                query += " AND c.period_start<='{0}' AND c.period_end>='{0}' ".format(datetime.now().strftime("%d-%m"))
                try:
                    percent = db.exec_query(query)['rows'][0]['percent']
                except:
                    percent = False
                #print int(percent['rows'][0]['percent'])
                #TODO ЧОЗАНАХ!?!???!
                if (not prow in self.percent) and percent:
                    #Проценты есть, а переменной нет -- блокируем ячейку и создаем переменную
                    item = self.ui.consumptionTableWidget.item(prow, 1)
                    item.setFlags(QtCore.Qt.NoItemFlags)
                    self.percent[prow] = percent
                    self.calc_brutto(prow)
                elif (prow in self.percent) and percent:
                    #Проценты есть и переменная есть -- меняем переменную
                    self.percent[prow] = percent
                elif (not percent) and (prow in self.percent):
                    #Процентов нет, а переменная есть -- разблокируем ячейку и удаляем переменную
                    item = self.ui.consumptionTableWidget.item(prow, 1)
                    item.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable)
                    del self.percent[prow]
                db.close_db()
            except:
                None
        elif pcell==2:
            #TODO проверяем если есть % то высчитываем
            self.calc_brutto(prow)

    def calc_brutto(self, prow):
        netto = int(self.ui.consumptionTableWidget.item(prow, 2).text())
        self.ui.consumptionTableWidget.item(prow, 1).setText("%s" % (100*netto/(100-self.percent[prow])))
        try:
            netto = int(self.ui.consumptionTableWidget.item(prow, 2).text())
            self.ui.consumptionTableWidget.item(prow, 1).setText("%s" % (100*netto/(100-self.percent[prow])))
        except:
            None

    def getSections(self):
        """Берет список разделов Menu_Class дубль"""
        db = localDb_Class()
        query = "SELECT DISTINCT s.id, s.name FROM section as s"
        vals = db.exec_query(query)['rows']
        db.close_db()
        return vals

    def getProducts(self):
        """Берет список разделов Menu_Class дубль"""
        db = localDb_Class()
        query = "SELECT DISTINCT p.id, p.name FROM product as p WHERE p.active"
        #Временно заменим запрос для заполнения рецептур
        #query = "SELECT DISTINCT p.id, p.name FROM product as p, income as i WHERE p.id=i.product AND i.count>0 AND i.active=1 AND p.active=1"
        vals = db.exec_query(query)['rows']
        db.close_db()
        return vals

    def saveData(self):
        #self.getVals()
        try:
            dish = self.getDish()
            vals = self.getVals()
            self.saveDish(dish)
            self.saveRow(vals, dish)
            self.close()
            self.parent.renew()
        except ValueError as e:
            print "err: ", e

    def getVals(self):
        vals = []
        #try:
        for row in range(self.ui.consumptionTableWidget.rowCount()):
            vals.append({
                "name":self.ui.consumptionTableWidget.cellWidget(row, 0).currentText(),
                "netto":self.ui.consumptionTableWidget.item(row, 2).text(),
                "brutto":self.ui.consumptionTableWidget.item(row, 1).text(),
                })
        #except:
            #raise ValueError("АТЕНШОН АТЕНШОН ВОЛК УНЕС ЗАЙЧАТ")
        return vals

    def getDish(self):
        vals = {
            "id":self.ui.idEdit.text(),
            "name":self.ui.nameEdit.text(),
            "section":self.ui.sectionBox.currentText(),
            "mass":self.ui.massEdit.text()
        }
        return vals

    def saveDish(self, val):
        db = localDb_Class()
        #query = "INSERT INTO dish"
        #db.exec_query(query)
        section = db.select_val_by_col("section", "name", "\'%s\'" % val["section"])["rows"][0]["id"]
        db.insert_val("dish", (val["name"], section, val["mass"]), iid=val["id"])
        db.close_db()

    def saveRow(self, vals, dish):
        db = localDb_Class()
        #query = "INSERT INTO "
        #db.exec_query(query)
        dish = db.select_val_by_col("dish", "name", "\'%s\'" % dish["name"])["rows"][0]["id"]
        for val in vals:
            product = db.select_val_by_col("product", "name", "\'%s\'" % val["name"])["rows"][0]["id"]
            db.insert_val("consumption", (dish, product, val["brutto"], val["netto"]))
        db.close_db()