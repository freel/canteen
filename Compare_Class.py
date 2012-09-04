# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from ui.Compare_Ui import Ui_Compare
from localDb_Class import localDb_Class
from Product_Class import Product_Class

class Compare_Class(QtGui.QDialog):
    """Сравнивает 2 набора данных,
    привязывает к первому набору второй"""
    def __init__(self, base_data=None, link_data=None, base_key=None, link_key='id', parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Compare()
        self.ui.setupUi(self)
        self.parent = parent

        self.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("saveData()"))
        self.connect(self.ui.addProductButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_addProductButton()"))

        self.get_data(base_data, link_data, base_key, link_key)
        self.compliteLinkBox()
        self.compliteForm()

    def renew(self):
        self.compliteLinkBox()

    def get_data(self, base_data, link_data, base_key, link_key):
        self.base_data, self.link_data, self.base_key, self.link_key = base_data, link_data, base_key, link_key
        self.data_rows = {}
        self.link_rows = {}

    def saveData(self):
        None

    def on_click_addProductButton(self):
        """Открывает приход"""
        form = Product_Class(self)
        form.show()

    def compliteForm(self):
        #Заполняет таблицу для привязки
        #второй столбик это линки, в комбобоксах
        for data_row in self.base_data:
            itemNumber = self.ui.compareTableWidget.rowCount()
            self.ui.compareTableWidget.setRowCount(itemNumber +1)
            self.data_rows[itemNumber] = {
                'base':data_row,
                'base_name':data_row['name'],
            }
            item = QtGui.QTableWidgetItem()
            item.setText("%s" % self.data_rows[itemNumber]['base_name'])
            item_link = QtGui.QComboBox()
            item_link.setEditable(True)
            item_link.setModel(self.listLink)
            item_link.setModelColumn(1)
            self.link_rows[itemNumber] = item_link
            self.connect(self.link_rows[itemNumber], QtCore.SIGNAL("currentIndexChanged(int)"),QtCore.SLOT("takeCell(int)"))

            self.ui.compareTableWidget.setItem(itemNumber, 0, item)
            self.ui.compareTableWidget.setCellWidget(itemNumber, 1, self.link_rows[itemNumber])

    def compliteLinkBox(self):
        #Заполняет комбобоксы
        self.listLink = QtGui.QStandardItemModel(0,2)
        for link in self.link_data:
            link_id = QtGui.QStandardItem("%s" % link[self.link_key])
            link_name = QtGui.QStandardItem(link['name'])
            self.listLink.appendRow([link_id, link_name])



class IncomeFrom1C_Class(Compare_Class):
    #Импорт из 1с
    def __init__(self, parent):
        Compare_Class.__init__(self, base_key="product", link_key="id",parent=parent)

    def get_data(self, base_data, link_data, base_key, link_key):
        self.base_data = self.get_data_from_file()
        self.link_data = self.get_data_from_product()
        self.base_key, self.link_key = base_key, link_key
        self.link_rows = {}
        self.data_rows = {}

    def get_data_from_file(self):
        #TODO загрузка из файла 1С както

        rows = ({
            'name':u'Морковь',
            'nomencature':'023423',
            'product':'',
            'measure':'166',
            'count':'27',
            'mass':'1000',
            'price':'41.23',
            },{
            'name':u'Семечка',
            'nomencature':'023445',
            'product':'',
            'measure':'166',
            'count':'15',
            'mass':'1000',
            'price':'57.14',
            })
        return rows

    def get_data_from_product(self):
        db = localDb_Class()
        query = "SELECT DISTINCT p.id, p.name FROM product as p WHERE p.active"
        vals = db.exec_query(query)['rows']
        db.close_db()
        return vals

    def saveData(self):
        for item in self.data_rows:
            try:
                base = self.data_rows[item]['base']
                base['product'] = int(self.listLink.item(self.ui.compareTableWidget.cellWidget(item,1).currentIndex(),0).text())
                base['rest'] = int(base['count'])*int(base['mass'])
                base['supplier'] = 1
                base['coefficient'] = 1
                base['shift'] = self.parent.parent.shift.shift
                keys = ",".join([key for key in base])
                vals = ",".join(["\'%s\'" % base[key] for key in base])
                query = "INSERT INTO income (id, %s, active, date) VALUES (Null, %s, 1, datetime('now', 'localtime'))" % (keys,vals)
                db = localDb_Class()
                db.exec_query(query)
                db.close_db()
            except:
                print "fui"