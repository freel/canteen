# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.Unload_Ui import Ui_Unload
from localDb_Class import localDb_Class
from lxml import etree

class Unload_Class(QtGui.QDialog):
    """Класс для работы с загрузкой выгрузкой данных"""
    #порядок импорта таблиц не ошибиться с названиями
    import_order = (
        'cashier',
        'shift',
        'measure',
        'supplier',
        'section',
        'product',
        'dish',
        'consumption',
        'income',
        'calculate',
        'menu',
        'company',
        'worker',
        'sale'
        )

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Unload()
        self.ui.setupUi(self)
        self.shift = parent.shift

        #self.connect(self.ui.formButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_formButton()"))
        self.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_saveButton()"))
        self.connect(self.ui.uploadButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_loadButton()"))

    #def on_click_formButton(self):
        #self.get_date()
        #self.export_base()

    def on_click_saveButton(self):
        self.get_date()
        self.export_base()

    def on_click_loadButton(self):
        self.import_base()

    def get_date(self):
        self.start = self.ui.startDateEdit.date().toString('yyyy-MM-dd 00:00:00')
        self.finish = self.ui.finishDateEdit.date().toString('yyyy-MM-dd 23:59:59')
        self.base = "1"

    def export_base(self):
        db = localDb_Class()

        root = etree.Element("root", base = self.base, start = self.start, finish = self.finish)
        tables = db.exec_query("SELECT name FROM sqlite_master WHERE type='table'")['rows']
        tables.remove(tables[1])
        for table in tables:
            #try:
                tableXML = etree.SubElement(root, "%s" % table[0])
                query = db.exec_query("SELECT * FROM {} WHERE date>='{}' AND date<='{}'".format(table[0],self.start,self.finish))
                rows, keys = query['rows'], query['keys']
                for row in rows:
                    id = etree.SubElement(tableXML, "id", value = "%s" % row["id"])
                    for key in keys:
                        id.append(etree.Element("data", field = "%s" % key, value = "%s" % row["%s" % key]))
            #except:
                #None
        db.close_db()
        with open('export/base_'+"%s" % self.shift.base+'.xml', 'w') as f:
            f.write(etree.tostring(root, pretty_print=True, encoding="UTF-8"))

    def import_base(self):
        db = localDb_Class()
        for table_tag in self.import_order:
            print table_tag
            element = etree.iterparse('import/base_'+self.shift.base+'.xml', events = ('end',), tag = table_tag)
            for event, elem in element:
                for element_id in elem.iter(tag="row"):
                    data = {i.get('field'):i.get('value') for i in element_id.iter(tag='data')}
                    getattr(self, 'import_%s' % table_tag)(data)
                elem.clear()
                while elem.getprevious() is not None:
                    del elem.getparent()[0]
            del element
        db.close_db()

    def check_value(self,table,val,col = 'id'):
        """Сравнивает на наличие подобной записи"""
        try:
            self.save_data(table,val)
        except:
            db = localDb_Class()
            answer = db.select_val_by_col(table,col,val[col])
            db.close_db()
            self.save_to_compare(answer['rows'],val)

    def save_data(self, table, val):
        """Записывает """
        db = localDb_Class()
        query = "INSERT INTO %s " % table
        query += " (%s) " % ",".join([ "%s" % field for field in val])
        query += " VALUES (%s) " % ",".join([ "'%s'" % val[field] for field in val])
        db.exec_query(query)
        db.close_db()

    def save_to_compare(self,exist_vals,changed_vals):
        """Сохраняет список для сравнения существующих записей"""
        None


    def import_cashier(self,val):
        self.check_value('cashier', val)

    def import_shift(self,val):
        None

    def import_measure(self,val):
        None

    def import_supplier(self,val):
        None

    def import_section(self,val):
        self.check_value('section', val)

    def import_product(self,val):
        self.check_value('product', val)

    def import_dish(self,val):
        self.check_value('dish', val)

    def import_consumption(self,val):
        self.check_value('consumption', val)

    def import_income(self,val):
        del val['base']
        self.check_value('income', val)

    def import_calculate(self,val):
        self.check_value('calculate', val)

    def import_menu(self,val):
        self.check_value('menu', val)

    def import_company(self,val):
        self.check_value('company', val)

    def import_worker(self,val):
        self.check_value('worker', val)

    def import_sale(self,val):
        self.check_value('product', val)
