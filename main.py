import sys
from datetime import date

from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QDialog, QLabel, QPushButton,
)

from DateBase import DateBase
from downloader import download
from generate_grafics import generate_grafics

download_ = download()
download_.download_currency()
date_now = date.today()
database = DateBase()
generate_grafics_ = generate_grafics()


class Beenance(QMainWindow):  # главный класс с интерфейсом и простыми функциями
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwin.ui", self)
        self.graf_win = Grafic_Window(self)
        self.initUI()

    def initUI(self):
        self.Today.setText(f'  {date_now}')
        self.set_text()
        self.usd_btn.clicked.connect(lambda: self.on_click('usd.txt'))
        self.euro_btn.clicked.connect(lambda: self.on_click('euro.txt'))
        self.pound_btn.clicked.connect(lambda: self.on_click('pound.txt'))
        self.tenge_btn.clicked.connect(lambda: self.on_click('tenge.txt'))

    def on_click(self, file):
        self.graf_win.file_currency = file
        generate_grafics_.generate_graf_month(file)
        generate_grafics_.generate_graf_alltime(file)
        self.graf_win.set_picture(file)
        print(self.graf_win.file_currency)
        self.graf_win.exec()

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

    # def open_grafic_win(self, file):


class Grafic_Window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: black")
        self.file_currency = ''
        self.setGeometry(640, 640, 640, 640)
        self.edit_field = QLabel(self)
        self.pixmap = QPixmap(f'images_currency\{self.file_currency.split(".")[0]}_month.png')
        self.edit_field.setPixmap(self.pixmap)

        self.month_btn = QPushButton(self)
        self.month_btn.setGeometry(100, 80, 100, 80)
        self.month_btn.setFont(QFont('Times', 10))
        self.month_btn.move(100, 470)
        self.month_btn.setText('Month')

        self.alltime_btn = QPushButton(self)
        self.alltime_btn.setGeometry(100, 80, 100, 80)
        self.alltime_btn.setFont(QFont('Times', 10))
        self.alltime_btn.move(450, 470)
        self.alltime_btn.setText('All Time')

        self.month_btn.setStyleSheet(
            'QPushButton{color: rgb(255, 255, 255); border: 2px solid;border-style:outset;border-radius:10px;border-color:rgb(0, 255, 255)}'\
            'QPushButton:hover{background-color:rgb(128, 128, 128);}')
        self.alltime_btn.setStyleSheet(
            'QPushButton{color: rgb(255, 255, 255); border: 2px solid;border-style:outset;border-radius:10px;border-color:rgb(0, 255, 255)}'\
            'QPushButton:hover{background-color:rgb(128, 128, 128);}')
        self.initUI()

    def initUI(self):
        self.month_btn.clicked.connect(lambda: self.on_click_('_month'))
        self.alltime_btn.clicked.connect(lambda: self.on_click_('_alltime'))

    def on_click_(self, date):
        self.pixmap = QPixmap(f'images_currency\{self.file_currency.split(".")[0]}{date}.png')
        print(f'images_currency\{self.file_currency.split(".")[0]}{date}.png')
        self.edit_field.setPixmap(self.pixmap)

    def set_picture(self, file_currency):
        self.pixmap = QPixmap(f'images_currency\{file_currency.split(".")[0]}_month.png')
        self.edit_field.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Beenance_app = Beenance()
    Beenance_app.show()
    sys.exit(app.exec())
