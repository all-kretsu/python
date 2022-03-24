
worker_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

names = []
for words in worker_list:
    for letters in words:
        
    words = words.lower()
    if 'игорь' or 'марина' or 'николай' in words:
        names.append('игорь', 'марина', 'николай')
  
