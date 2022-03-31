# Создать вручную список с ценами на товары, указать окончания в руб. и коп.


price = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
         70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
         8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

for prices in sorted(price):
    if type(prices) == float:
        r, k = str(prices).split('.')
        if len(k) == 1:
            k = k + '0'
        prices = f'{r} руб. {k} коп.'
    else:
        r = str(prices)
        prices = f'{r} руб.'
    print(prices)
    # список отсортированный в обратном порядке
    price_2 = sorted(price, reverse= True)

print(price)
print(price_2)