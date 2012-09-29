# -*- coding: utf-8 -*-

import sqlite3

class csvtosqlite():
    """Работает с базой данных"""

    def __init__(self):
        self.file = "../base.db"
        self.open_db()
        self.exec_query("PRAGMA foreign_keys = ON")

    def open_db(self):
        """Открывает базу данных, или создает её, если не существует"""
        self.connection = sqlite3.connect(self.file)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def close_db(self):
        """Закрывает базу, записывает изменения"""
        #self.cursor.close()
        self.connection.commit()
        self.connection.close()

    def exec_query(self,query,*rowId):
        """Выполняет запрос, аргументы: запрос и список переменных"""
        value = ()
        keys = ()
        try:
            self.cursor.execute(query,rowId) if rowId else self.cursor.execute(query)
            value = self.cursor.fetchall()
            if self.cursor.description:
                keys = [tuple[0] for tuple in self.cursor.description]
            return {"rows":value,"keys":keys}
        except sqlite3.Error as e:
            raise Exception("Ошибка выполнения запроса:", e.args[0])

    def getcompany(self):
        csv = open("predpr.csv")
        table = "company"
        for line in csv:
            try:
                query = "INSERT INTO %s " % table
                query += " (id, name, coefficient, active, date) VALUES "
                values = ",".join(["'%s'" % j for j in line[:-1].split(";") ])
                query += " (%s, 1, datetime('now', 'localtime'))" % values
                print query
                self.exec_query(query)
            except:
                print "mimimi"

    def getworker(self):
        csv = open("card.csv")
        table = "worker"
        for line in csv:
                query = "INSERT INTO %s " % table
                query += " (id, company, card, name, employee, active, date) VALUES "
                l = line.split(";")
                values = "'%s', '%s', '%s', '%s', '%s'" % (l[3],'{:0>16}'.format(l[0]),l[2],l[1],l[5])
                query += " (NULL, %s, datetime('now', 'localtime'))" % values
                print query
                self.exec_query(query)

    def getproducts(self):
        csv = open("products.csv")
        table = "product"
        for line in csv:
            try:
                query = "INSERT INTO %s " % table
                query += " (id, name, active, date) VALUES "
                values = "'%s'" % line[:-1]
                query += " (Null, %s, 1, datetime('now', 'localtime'))" % values
                print query
                self.exec_query(query)
            except:
                print "mimimi"

if __name__ == "__main__":
    db = csvtosqlite()
    db.getcompany()
    db.getworker()
    db.getproducts()
    db.close_db()
