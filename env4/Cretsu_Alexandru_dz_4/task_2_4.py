"""Этот модуль выводит курс обозначенной валюты"""


import requests


def currency_rate(currency):
    # get http
    cur_rate = requests.get('http://cbr.ru/scripts/XML_daily.asp').text
    # split in list result of http
    rate_lst = list(cur_rate.split('ID'))
    # get requested value
    numb = [x.split('Value') for x in rate_lst if currency in x]
    # split requested value
    for y in numb:

        print(y[-2])
    # print(''.join(numb))


currency_rate('MDL')
