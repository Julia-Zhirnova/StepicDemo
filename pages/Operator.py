from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem,
    QTableWidget,
    QWidget  # для работы с таблицами
)

import sqlite3

class Operator(QDialog):
    def __init__(self, table_widget):        
        super(Operator, self).__init__()
        print("Проверка открытия страницы оператора")
         # ÐÐ½Ð¸ÑÐ¸Ð°Ð»Ð¸Ð·Ð¸Ñ€ÑÐµÐ¼ Ð¾Ð±ÑÑÑ ÑÐ°Ð±Ð»Ð¸ÑÑ
        self.tableVseZayavki = table_widget
        #self.tableVseZayavki = self.findChild(QTableWidget, 'tableVseZayavki')
        self.showdata()

    def showdata(self):
        conn1 = sqlite3.connect("uchet.db")
        cur1 = conn1.cursor()
        data = cur1.execute("SELECT * FROM requests")
        col_name = [i[0] for i in data.description]
        print(col_name)
        data_rows = data.fetchall()
        self.tableVseZayavki.setColumnCount(len(col_name))
        print(len(col_name))
        
        self.tableVseZayavki.setHorizontalHeaderLabels(col_name)
        self.tableVseZayavki.setRowCount(0)       
        for i, row in enumerate(data_rows):
            self.tableVseZayavki.setRowCount(self.tableVseZayavki.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableVseZayavki.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableVseZayavki.resizeColumnsToContents()
        conn1.commit()
        conn1.close()