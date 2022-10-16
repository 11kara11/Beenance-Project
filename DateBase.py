class DateBase():   # класс базы данных, тут осуществляется работа с значениями валют
    def __init__(self):
        self.date_value = {}


    def read_quotes(self, file_currency):  # читает котировки

        with open(f'currency\{file_currency}', 'r') as fout:
            lines = fout.readlines()
            for i in lines:
                i = i.split('|')
                self.date_value[(i[2]).replace('\n', '')] = float(i[1].replace(',', '.'))
        return self.date_value
    def last_value(self):
        return list(self.date_value.items())[-1]
