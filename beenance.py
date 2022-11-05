import os
import sys
import time
from datetime import date, datetime

from PyQt5 import uic, QtCore
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QDialog, QLabel, QPushButton, QLineEdit
)

from DataBase import DataBase
from downloader import download
from generate_grafics import generate_grafics

download_ = download()
date_now = date.today()
database = DataBase()
generate_grafics_ = generate_grafics()

database.check_files()

year_today, month_today, day_today = str(date_now).split('-')
c_time = os.path.getmtime('currency\\usd.txt')
date_last_upgrade = time.ctime(c_time)
date_last_upgrade = date_last_upgrade[4:].replace('  ', ' ')
date_last_upgrade = datetime.strptime(date_last_upgrade, '%b %d %H:%M:%S %Y')
datetime_upgrade = datetime(int(year_today), int(month_today), int(day_today), 17, 0, 0)
if datetime_upgrade <= datetime.now() and datetime_upgrade >= date_last_upgrade:
    download_.download_currency()
    print('download currency')

diff_date = datetime.now() - date_last_upgrade
print(diff_date)

if 'day' in str(diff_date):
    download_.download_currency()
    print('download currency for the past days')
'''
выше находится "ленивая загрузка", проверяет, скачивались ли сегодня новые данные

класс Beenance - главный экран с отображением валют
класс Grafic_Window - диалоговое окно, которое открывается по нажатию одной из кнопок класса Beenance
'''


class Beenance(QMainWindow):  # главный класс с интерфейсом и простыми функциями
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwin.ui", self)
        self.graf_win = Grafic_Window(self)
        self.initUI()

    def initUI(self):
        self.Today.setText(f'  {date_now}')
        self.set_text()
        self.setWindowTitle('Beenance')
        self.usd_btn.clicked.connect(lambda: self.on_click('usd.txt'))
        self.euro_btn.clicked.connect(lambda: self.on_click('euro.txt'))
        self.pound_btn.clicked.connect(lambda: self.on_click('pound.txt'))
        self.tenge_btn.clicked.connect(lambda: self.on_click('tenge.txt'))

    def on_click(self, file):
        self.graf_win.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.graf_win.setWindowTitle(file.split('.')[0])
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

        self.tenge_line = QLineEdit(self)
        self.tenge_line.setText('')
        self.tenge_line.setGeometry(350, 50, 350, 50)
        self.tenge_line.move(200, 570)
        self.tenge_line.setStyleSheet('color: rgb(255, 255, 255)')
        self.tenge_line.setReadOnly(True)
        self.tenge_line.setFrame(False)

        self.month_btn.setStyleSheet(
            'QPushButton{color: rgb(255, 255, 255); border: 2px solid;border-style:outset;border-radius:10px;border-color:rgb(0, 255, 255)}' \
            'QPushButton:hover{background-color:rgb(128, 128, 128);}')
        self.alltime_btn.setStyleSheet(
            'QPushButton{color: rgb(255, 255, 255); border: 2px solid;border-style:outset;border-radius:10px;border-color:rgb(0, 255, 255)}' \
            'QPushButton:hover{background-color:rgb(128, 128, 128);}')
        self.initUI()

    def initUI(self):
        self.month_btn.clicked.connect(lambda: self.on_click_('_month'))
        self.alltime_btn.clicked.connect(lambda: self.on_click_('_alltime'))

    def on_click_(self, date):
        self.pixmap = QPixmap(f'images_currency\{self.file_currency.split(".")[0]}{date}.png')
        print(f'images_currency\{self.file_currency.split(".")[0]}{date}.png')
        self.edit_field.setPixmap(self.pixmap)
        if self.file_currency == 'tenge.txt':
            self.tenge_line.setText('Цена за 100 единиц валюты')
        else:
            self.tenge_line.setText('')

    def set_picture(self, file_currency):
        self.pixmap = QPixmap(f'images_currency\{file_currency.split(".")[0]}_month.png')
        if file_currency == 'tenge.txt':
            self.tenge_line.setText('Цена за 100 единиц валюты')
        else:
            self.tenge_line.setText('')
        self.edit_field.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Beenance_app = Beenance()
    Beenance_app.show()
    sys.exit(app.exec())
