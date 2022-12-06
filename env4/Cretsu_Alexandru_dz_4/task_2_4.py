"""Этот модуль выводит курс обозначенной валюты"""


import requests


def currency_rate(currency):
    # get http
    cur_rate = requests.get('http://cbr.ru/scripts/XML_daily.asp').text
    # split in list result of http
    rate_lst = cur_rate.split('ID')
    # get and split requested value, make argument to upper case
    numb = [x.split('Value>') for x in rate_lst if currency.upper() in x]
    for y in numb:
        z = y[-2].split('</')
        print(''.join(z))


currency_rate('mdl')
