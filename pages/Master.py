from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

class Master(QDialog):
    def __init__(self):        
        super(Master, self).__init__()
        print("Проверка открытия страницы мастера")