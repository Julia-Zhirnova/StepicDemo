from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem
)

import sqlite3

class Zakazchik(QDialog):
    def __init__(self, table_widget):        
        super(Zakazchik, self).__init__()
        print("Проверка открытия страницы заказчика")
         # ÐÐ½Ð¸ÑÐ¸Ð°Ð»Ð¸Ð·Ð¸Ñ€ÑÐµÐ¼ Ð¾Ð±ÑÑÑ ÑÐ°Ð±Ð»Ð¸ÑÑ
        self.tableZakazchikaZayavki = table_widget
        #self.tableVseZayavki = self.findChild(QTableWidget, 'tableVseZayavki')
        self.showdata()

    def showdata(self):
        conn1 = sqlite3.connect("uchet.db")
        cur1 = conn1.cursor()
        data = cur1.execute("SELECT * FROM requests")
        col_name = [i[0] for i in data.description]
        print(col_name)
        data_rows = data.fetchall()
        self.tableZakazchikaZayavki.setColumnCount(len(col_name))
        print(len(col_name))
        
        self.tableZakazchikaZayavki.setHorizontalHeaderLabels(col_name)
        self.tableZakazchikaZayavki.setRowCount(0)       
        for i, row in enumerate(data_rows):
            self.tableZakazchikaZayavki.setRowCount(self.tableZakazchikaZayavki.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableZakazchikaZayavki.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableZakazchikaZayavki.resizeColumnsToContents()
        conn1.commit()
        conn1.close()