# importing the requests library
import requests
def download(codevalue, value_change_step, to):
    #codevalue = "USDRUB"
    from_date = "4.10.2010"
    #to = "10.10.2022"
    #value_change_step = "10"

    # получение данных из чисел
    df = from_date.split(".")[0]
    mf = str(int(from_date.split(".")[1])-1)
    yf = from_date.split(".")[2]

    dt = to.split(".")[0]
    mt = str(int(to.split(".")[1])-1)
    yt = to.split(".")[2]


    print(f"{df}, {mf}, {yf}")
    print(f"{dt}, {mt}, {yt}")
    """
    
    value_change_step важная переменная, от неё зависит шаг изменения валюты в файл
    1 - тик
    2 - 1 мин
    3 - 5 мин
    4 - 10 мин
    5 - 15 мин
    6 - 30 мин
    7 - 1 час
    8 - 1 день
    9 - 1 неделя
    10 - 1 месяц
    
    to переменная отвечает за дату <<до какого периода>>
    from_date переменная отвечает за дату <<с чего начать>>
    
    codewalue переменная, которая отвечает за сами валюты, относительно кого (например <<USDRUB>>, или <<RUBEUR>>)
    
    
    
    после 4 запятой и между 5 запятой и есть сам курс числа за нужный период времени
    """

    # api-endpoint
    URL = f"https://export.finam.ru/export9.out?market=5&em=901&token=03AIIukzgFeP2OY8aYJVZwgJdbmel4oU-92-Fn6F-MVxfiWotcIUlmQiAVKFCsk9AWxUXkZxTCC744hd0GHmdbFycGpqAoFWptkeqOUnNHECkntaMNdLG6cJRwG7tgoqQgdFU4o3YIfsPlirYNzTyZnsjI02Y_rJjeNaLHwnCvPJRxbL7U8HMpTfbChiCZFu-J5GjQW5v6yal-VudobN4XnhnuNUUFr_dP5DPeW4aCwLHqLGuWBCRlxMM1MSDUwkGfHaHzLZxd1Xsr3-9jT8j-RBc_JLwW0CVrREl-ZZq41qYSlFwGF9zWMk_pizzTL8Is_wrtZsm6S2dRyglwwyLfAQVF6AyIvO0JiUBPkoO-lx-g4NO2ij3YQM19JSEkALh6r786cPW-0FnF9I2eETmcopaWBzfmYyWOz8Mj4vpOR-BzHhIRLna9NPepjlNpgyLxdUn_nZcPFnkLku0r9WJZC1cuRo1tccISz_epmPiqBWfX58xJ4KQrbpITf32Anw_DpPS8fJp1e3Ze&code={codevalue}&apply=0&df={df}&mf={mf}&yf={yf}&from={from_date}&dt={dt}&mt={mt}&yt={yt}&to={to}&p={value_change_step}&f=file_kotirofka&e=.txt&cn={codevalue}&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' }
    # sending get request and saving the response as response object
    r = requests.get(url=URL, headers=headers)
    print(r)

    with open('test.txt', 'wb') as f:
        f.write(r.content)

download("USDRUB", '10', '13.10.2022')