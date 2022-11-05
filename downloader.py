import os
import sys
import xml.etree.ElementTree as ET
from datetime import date

import requests
from PyQt5 import QtWidgets

"""


Всё относительно в российских рублях

Ниже переменные типо date_from (от какой даты), date_to (до какой даты), 
value_code (код валюты: https://cbr.ru/scripts/XML_val.asp?d=0)
А так же code_dictionary, пополнять его для опознания валюты

CBR даёт данные только в днях :|

downloader -  скачивает и записывает валюты по переданным аргументам
download_currency - вспомогательная функция которая автоматизирует скачивание валют по словарю
"""


class download():
    def __init__(self):
        self.code_dictionary = {"R01239": "euro.txt",
                                "R01235": "usd.txt",
                                'R01035': 'pound.txt',
                                'R01335': 'tenge.txt'}

    def downloader(self, date_to, value_code, file_currency):
        date_from = "02/03/2001"

        URL = f"https://cbr.ru/scripts/XML_dynamic.asp?date_req1={date_from}&date_req2={date_to}&VAL_NM_RQ={value_code}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        try:
            r = requests.get(url=URL, headers=headers)
        except requests.ConnectionError:
            print('connection dissable')
            self.show_Error('connection dissable')
            sys.exit()
        except requests.RequestException:
            print('general error')
            self.show_Error('general error of programm')
            sys.exit()
        except KeyboardInterrupt:
            print('someone closed programm')
            self.show_Error('someone closed programm')
            sys.exit()

        with open('info.xml', 'wb') as f:
            f.write(r.content)  # сам xml файл

        root_node = ET.parse('info.xml').getroot()

        with open(f'currency\{file_currency}', 'w') as d:
            for tag in root_node.findall('Record'):
                d.write(
                    f"{self.code_dictionary[tag.attrib['Id']]}|{list(tag)[1].text}|{tag.attrib['Date']}\n")  # сначала валюта, потом цена, и после уже дата
        os.remove('info.xml')

    def download_currency(self):
        for i in range(4):
            value_code, file_currency = list(self.code_dictionary.items())[i]
            year, month, day = str(date.today()).split('-')
            date_to = '/'.join([day, month, year])
            self.downloader(date_to, value_code, file_currency)

    def show_Error(self, error):
        app = QtWidgets.QApplication([])
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(error)
        error_dialog.setWindowTitle("connection error")
        app.exec()
