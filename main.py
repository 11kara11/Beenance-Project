import sys
from datetime import date

from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)

from DateBase import DateBase
from downloader import download

download = download
date_now = date.today()
database = DateBase()
class Beenance(QMainWindow):   # главный класс с интерфейсом и простыми функциями
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwin.ui", self)
        self.initUI()

    def initUI(self):
        self.Today.setText(f'  {date_now}')
        self.set_text()
    def set_text(self):
        for i in ['euro.txt', 'pound.txt', 'tenge.txt', 'usd.txt']:
            database.read_quotes(i)
            date, value = database.last_value()
            if i == 'euro.txt':
                self.euro_line.setText(f' {value}  ₽')
            if i == 'pound.txt':
                self.pound_line.setText(f' {value}  ₽')
            if i == 'tenge.txt':
                self.tenge_line.setText(f' {str(value / 100)[:7]}  ₽')
            if i == 'usd.txt':
                self.usd_line.setText(f' {value}  ₽')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    Beenance_app = Beenance()
    Beenance_app.show()
    sys.exit(app.exec())
