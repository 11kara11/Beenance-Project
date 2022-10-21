import statistics


class DateBase():   # класс базы данных, тут осуществляется работа с значениями валют
    def __init__(self):
        self.date_value = {}
        self.mean_value = []


    def read_quotes(self, file_currency):  # читает котировки
        with open(f'currency\{file_currency}', 'r') as fout:
            lines = fout.readlines()
            for i in lines:
                i = i.split('|')
                self.date_value[(i[2]).replace('\n', '')] = float(i[1].replace(',', '.'))
        return self.date_value
    def last_value(self):
        return list(self.date_value.items())[-1]

    def mean_value_year(self, file_currency):
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
            if temp_year[-1] == 2022:
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


a = DateBase()
a.value_month('usd.txt')