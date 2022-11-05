# Beenance-Project
Проектик на PyQt5, отслеживание валют с графиками
https://disk.yandex.ru/d/1Ilw-au0diw5CA - ссылка на exe
# Фичи
Главный экран, на котором находятся валюты(расположены вручную)
по нажатию на валюту будет открываться окно валюты с графиком за все время и за последние 31 месяц ( используем библиотеку matplotlib )

котировки берутся с CBR
парсятся по дням и обновляются при запуске(среднее время запуска проги < 1сек)

Бета версия подразумевает 4 валюты(USD TENGE POUND EUR)

CBR НЕ РАБОТАЕТ НА ВЫХОДНЫХ(((

# dependencies
matplotlib.pyplot
PyQT5
requests

version in 'requirements.txt'

# Design
![image](https://user-images.githubusercontent.com/110305715/198326043-6498c3d9-fc30-49a9-84b1-7caa62d8e7f3.png)

