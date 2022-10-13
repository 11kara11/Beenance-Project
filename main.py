from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLineEdit, QLabel, QPushButton,
    QMainWindow
)
from PyQt5 import uic
import sys
from datetime import date

date_now = date.today()
class Beenance(QMainWindow):   # главный класс с интерфейсом и простыми функциями
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwin.ui", self)
        self.initUI()

    def initUI(self):
        self.Today.setText(f'  {date_now}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Beenance_app = Beenance()
    Beenance_app.show()
    sys.exit(app.exec())
