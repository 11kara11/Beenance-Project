import datetime
import os
import statistics
import sys

from PyQt5 import QtWidgets

from downloader import download

'''
класс с чтением txt

read_quotes - возвращает dict с датами и валютами

last_value - возвращает последние полученное с CBR значение

mean_value_year - возвращает списки годов и средних значений валюты за эти годы

value_month - возвращает список дат с прыжком через 5 дней и среднее значение за этот прыжок, все ограничивается 30 днями


'''

download_ = download()


class DataBase():  # класс базы данных, тут осуществляется работа с значениями валют
    def __init__(self):
        self.date_value = {}
        self.mean_value = []
        self.data_list = ['usd.txt', 'euro.txt', 'pound.txt', 'tenge.txt']
        self.main_files = ['mainwin.ui', 'currency', 'images_currency', 'usd.txt', 'euro.txt', 'pound.txt', 'tenge.txt']

    def read_quotes(self, file_currency):  # читает txt
        with open(f'currency\{file_currency}', 'r') as fout:
            lines = fout.readlines()
            for i in lines:
                i = i.split('|')
                self.date_value[(i[2]).replace('\n', '')] = float(i[1].replace(',', '.'))
        return self.date_value

    def last_value(self):
        return list(self.date_value.items())[-1]

    def mean_value_year(self, file_currency):
        self.mean_value = []
        temp_value = []
        temp_year = []
        with open(f'currency\{file_currency}', 'r') as fout:
            lines = fout.readlines()
            for i in lines:
                year = int((i.split('|')[2]).split('.')[2].replace('\n', ''))
                if year not in temp_year:
                    if temp_value == []:
                        temp_year.append(year)
                        i = float(i.split('|')[1].replace(',', '.'))
                        temp_value.append(i)
                    else:
                        self.mean_value.append(statistics.mean(temp_value))
                        temp_value = []
                else:
                    i = float(i.split('|')[1].replace(',', '.'))
                    temp_value.append(i)
            if temp_year[-1] == 2023:
                self.mean_value.append(statistics.mean(temp_value))
        return self.mean_value, temp_year

    def value_month(self, file_currency):
        dates = []
        values = []
        with open(f'currency\{file_currency}', 'r') as fout:
            lines = fout.readlines()[:-25: -3]
            for i in lines:
                dates.append('.'.join((i.split('|')[2]).split('.')[0:2]))
                values.append(float(i.split('|')[1].replace(',', '.')))
        dates.reverse()
        values.reverse()
        return dates, values

    def check_files(self):
        for i in self.main_files:
            if i in self.data_list:
                if os.path.isfile(f'currency\{i}') == False:
                    download_.download_currency()
            elif os.path.exists(i) == False:
                self.show_Error('OoOpS, someone deleted main folder/files, u need reinstall Beenance' + i)
                sys.exit()
        for file_currency in self.data_list:
            with open(f'currency\{file_currency}', 'r') as fout:
                lines = fout.readlines()
                if lines == []:
                    download_.download_currency()
                print('begin checked')
                try:
                    for i in lines:
                        i = i.rstrip('\n')
                        name_file, value, date = i.split('|')
                        if name_file not in self.data_list:
                            download_.download_currency()
                            print('type error of txt')
                            break
                        elif value.replace(',', '', 1).isdigit() == False:
                            download_.download_currency()
                            print('type error of value')
                            break
                        datetime.datetime.strptime(date, '%d.%m.%Y')
                except Exception:
                    print(1)
                    download_.download_currency()

    def show_Error(self, error):
        app = QtWidgets.QApplication([])
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(error)
        error_dialog.setWindowTitle("directory error")
        app.exec()
