import requests


def currency_rate(currency):
    cur_rate = requests.get('http://cbr.ru/scripts/XML_daily.asp').text
    rate_lst = list(cur_rate.split('ID'))
    print(rate_lst)
    for i in rate_lst:
        numb = [float(x) for x in i.split() if x.isdigit()]
        if currency in i:
            print(numb)


currency_rate('MDL')
