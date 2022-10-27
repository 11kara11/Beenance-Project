import matplotlib.pyplot as plt

from DateBase import DateBase

database = DateBase()
'''
Класс с генерацией графиков с помощбю библиотеки matplotlib
на вход к графикам поступают списки с датами/годами из DateBase
'''


class generate_grafics():
    def __init__(self):
        pass

    def generate_graf_alltime(self, file_name):
        y, x = database.mean_value_year(file_name)
        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.savefig((f'images_currency\{file_name.split(".")[0]}_alltime.png'))

    def generate_graf_month(self, file_name):
        x, y = database.value_month(file_name)
        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.savefig((f'images_currency\{file_name.split(".")[0]}_month.png'))
