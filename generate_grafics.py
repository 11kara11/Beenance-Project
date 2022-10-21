import matplotlib.pyplot as plt
from DateBase import DateBase


database = DateBase()


class generate_grafics():
    def __init__(self):
        pass

    def generate_graf_alltime(self, file_name):
        y, x = database.mean_value_year(file_name)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()
    def generate_graf_month(self, file_name):
        x, y = database.value_month(file_name)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()

a = generate_grafics()
a.generate_graf_alltime('usd.txt')