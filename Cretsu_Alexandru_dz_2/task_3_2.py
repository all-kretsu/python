
worker_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']


for words in worker_list:
    for letter in words:
        if letter != ' ':
            print(letter[-1:])
        else:
            pass