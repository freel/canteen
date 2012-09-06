# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.Income_Ui import Ui_Income
from localDb_Class import localDb_Class
from Shift_Class import Shift
from Product_Class import Product_Class


class Income_Class(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Income()
        self.ui.setupUi(self)
        self.parent = parent
        #DAS MODEL#
        self.listProduct = QtGui.QStandardItemModel(0,2)
        self.ui.productEdit.setModel(self.listProduct)
        self.ui.productEdit.setModelColumn(1)
        self.listMeasure = QtGui.QStandardItemModel(0,2)
        self.ui.measureBox.setModel(self.listMeasure)
        self.ui.measureBox.setModelColumn(1)

        self.fillIncome()

        self.connect(self.ui.saveIncomButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_saveIncomeButton()"))
        self.connect(self.ui.addProductButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_addProductButton()"))
        #self.connect(self.ui.listProductView, QtCore.SIGNAL("currentRowChanged(int)"), QtCore.SLOT("on_changeProduct()"))
        #self.connect(self.ui.checkBoxGoods, QtCore.SIGNAL("stateChanged(int)"),QtCore.SLOT("isGoods()"))
        self.connect(self.ui.measureBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.setMass)

    def renew(self):
        self.listProduct.clear()
        map(self.setProduct,self.getProduct())

    def on_click_addProductButton(self):
        """Открывает приход"""
        form = Product_Class(self)
        form.show()

    def on_click_saveIncomeButton(self):

        self.saveData(self.getParamsFromWindow())
        self.close()
        self.parent.renew()

    def getParamsFromWindow(self):
        """Происходит сбор параметров:
            name наименование продукта в поставке
            product номер продукта в справочнике продуктов
            measure еденица измерения продукта
            count количество продукта в зависимости от единицы измерения
            (картошка - кг, например 30кг картошки)
            mass масса единицы продукта в граммах
            (на единицу килограмма картошки - 1000г)
            rest остаток на складе в граммах
            supplier поставщик(на всякий случай)
            price цена за единицу товара
            coefficient ???
            for_sale флаг отоварки TRUE отоварка, False не отоварка
            shift смена в которую был зарегистрирован приход

            TODO как продать 1024г картошки например??? И надо ли?
        """
        name = self.ui.nameEdit.text()
        nomenclature = int(self.ui.nomenclatureEdit.text())
        product = int(self.listProduct.item(self.ui.productEdit.currentIndex(),0).text())
        measure = int(self.listMeasure.item(self.ui.measureBox.currentIndex(),0).text())
        count = self.ui.countEdit.text()
        mass = self.ui.massEdit.text()
        rest = float(mass)*int(count)
        supplier = 1
        price = self.ui.priceEdit.text()
        coefficient = 1
        #~ for_sale = self.ui.checkBoxGoods.isChecked()
        shift = self.parent.parent.shift
        param = (name,nomenclature,product,measure,count,mass,rest,supplier,price,coefficient,shift.shift,)
        return param

    def fillIncome(self):
        """
        Заполнение прихода
        """
        map(self.setProduct,self.getProduct())
        map(self.setMeasure,self.getMeasure())
        self.setMass(0)


    def setProduct(self,row):
        """Вставляет продукт в список"""
        num = QtGui.QStandardItem("%s" % row[0])
        nam = QtGui.QStandardItem(row[1])
        self.listProduct.appendRow([num,nam])
        #self.ui.listProductView.insertItem(row[0],row[1])

    def setMeasure(self,row):
        """Вставляет Единицы измерения"""
        num = QtGui.QStandardItem("%s" % row[0])
        nam = QtGui.QStandardItem(row[1])
        self.listMeasure.appendRow([num,nam])

    def getProduct(self):
        """Выбирает список продуктов"""
        db = localDb_Class()
        val = [(t['id'],t['name']) for t in db.select_all_val('product')['rows']]
        db.close_db()
        return val

    def getMeasure(self):
        """Выбирает единицы измерения"""
        db = localDb_Class()
        self.measure = [(t['code'],t['name'],t['defmass']) for t in db.select_all_val('measure')['rows']]
        db.close_db()
        return self.measure

    def setMass(self,num):
        self.ui.massEdit.setText("%s" % self.measure[num][2])

    def saveData(self,data):
        """Сохраняет данные"""
        db = localDb_Class()
        db.insert_val('income',data)
        db.close_db()

    def on_changeProduct(self):
        if self.ui.nameEdit.isReadOnly():
            self.ui.nameEdit.setText(self.ui.listProductView.currentItem().text())

    def isGoods(self):
        self.ui.nameEdit.setReadOnly(True)
        #self.ui.nameEdit.setText(self.ui.listProductView.currentRow())

    def keyPressEvent(self, event):
        """Назначение клавиш"""
        try:
            {QtCore.Qt.Key_F9:self.ui.addProductButton.emit,
            QtCore.Qt.Key_F12:self.ui.saveIncomButton.emit,
            }[event.key()](QtCore.SIGNAL("clicked()"))
        except KeyError as e:
            None
