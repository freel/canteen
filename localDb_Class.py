# -*- coding: utf-8 -*-

import sqlite3
from datetime import datetime

class localDb_Class():
    """Работает с базой данных"""

    def __init__(self):
        self.file = "base.db"
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
        #print query
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


    def create_all_tables(self):
        """
            Создание таблиц, берем словарик и смотрим значения
            Таблица income
                for_sale        BOOLEAN, --флаг отоварки
            Таблица shift
                period          INT, --флаг периода дня (завтрак=0, обед=1, ужин=2)
        """

        f = open("run.sql","r")
        query = f.read()
        try:
            self.cursor.executescript(query)
        except sqlite3.Error as e:
            print ("Ошибка выполнения запроса:", e.args[0])


    def insert_val(self,table,data):
        """
        Вставляет данные в таблицу
        """
        query = "INSERT INTO "
        query += table
        query += " VALUES (NULL,"
        query += ",".join("\"" + "%s" % val + "\"" for val in data)
        query += ", 1, datetime('now', 'localtime'))"
        self.exec_query(query)
        return True

    def select_all_val(self,table):
        """
        Берет данные со всей таблицы
        Возвращает списки значений
        """
        query = "SELECT * FROM "
        query += table
        query += " WHERE active"
        return self.exec_query(query)


    def select_val_by_id(self,table,rowId):
        """
        По списку ID возвращает список данных
        """
        query = "SELECT * FROM "
        query += table
        query += " WHERE id=?"
        return self.exec_query(query,rowId)

    def select_val_by_col(self,table,colname,colval):
        """
        По списку ID возвращает список данных
        """
        query = "SELECT * FROM "
        query += table
        query += " WHERE "
        query += colname + "=" + colval
        return self.exec_query(query)

    def update_val_by_id_name(self,table,rowId,name,val):
        """
        Вносит изменения в одну запись одной строки
        """
        query = "UPDATE "
        query += table + " SET "
        query += name + "=\'" + "%s" % val + "\'"
        query += " WHERE id=?"
        return self.exec_query(query,rowId)

    def update_row_by_id(self,table,*vals):
        """
        Вносит изменения в строку
        """
        query = "UPDATE "
        query += table + " SET ("
        query += ",".join(["\"" + name + "\"" for name in names])
        query += ") VALUES ("
        query += ",".join(["\"" + "%s" % val + "\"" for val in vals])
        query += ") WHERE id=?"
        return self.exec_query(query,rowId)

    def del_row_by_id(self,table,rowId):
        """
        Ставит отметку о том что запись удалена
        """
        query = "UPDATE "
        query += table + " SET "
        query += " active=0 "
        query += " WHERE id=?"
        return self.exec_query(query,rowId)

    def select_col_names(self,table):
        """Выбирает список имен столбцов"""
        query = "PRAGMA table_info("
        query += table + ")"
        val = self.exec_query(query)
        return val

    def export_from_file(self,filename):
        """Заполняет данными из файла .data"""
        f = open(filename,"r")
        for line in f.readlines():
            self.insert_val(line.strip(" \t\n").split(",")[0],line.strip(" \t\n").split(",")[1:])


    def get_first_shift(self):
        """Находит первую смену"""
        return self.select_val_by_col('shift','shift','1')['rows'][0]

    def select_consumption(self,dishId):
        """Выбирает состав продукта"""
        query = "SELECT SUM(i.price*i.coefficient*c.brutto/1000) as price "
        query += "FROM consumption as c, product as p, income as i WHERE "
        query += "c.product = p.id AND i.product=p.id AND c.dish=" + "\'%s\'" % dishId
        return self.exec_query(query)

if __name__ == "__main__":
    db = localDb_Class()
    db.open_db()

    db.create_all_tables()
    db.export_from_file("simple.data")

    db.close_db()
