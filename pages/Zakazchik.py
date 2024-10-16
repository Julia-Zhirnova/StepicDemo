from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

class Zakazchik(QDialog):
    def __init__(self):        
        super(Zakazchik, self).__init__()
        print("Проверка открытия страницы заказчика")