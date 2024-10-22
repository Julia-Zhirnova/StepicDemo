from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem  # для работы с таблицами
)

import sqlite3

class Operator(QDialog):
    def __init__(self, table_widget):        
        super(Operator, self).__init__()
        print("Проверка открытия страницы оператора")
        self.tableVseZayavki = table_widget
        print(self.tableVseZayavki)
        print(table_widget)
        self.showdata()

    def showdata(self):
        conn1 = sqlite3.connect("uchet.db")
        cur1 = conn1.cursor()
        data = cur1.execute(f"""SELECT
                                IDrequest AS "Идентификатор заявки",
                                startDate AS "Дата начала заявки",
                                orgTechTypeID AS "ID типа техники",
                                orgTechModel AS "Модель техники",
                                problemDescryption AS "Описание проблемы",
                                requestStatusID AS "ID статуса заявки",
                                completionDate AS "Дата завершения",
                                repairParts AS "Замененные запчасти",
                                masterID AS "ID мастера",
                                clientID AS "ID клиента"
                                FROM requests;""")
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