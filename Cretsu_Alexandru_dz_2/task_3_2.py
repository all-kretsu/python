# Задание 3
# Выделить из списка имена и создать их приветствие

worker_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

# Метод со списком
names = []
for words in worker_list:
    new_list = []
    words = words.lower()
    new_list.append(words.split(' '))
    for elements in new_list:
        names.append(elements[-1])

for persons in names:
    print(f'Привет {persons.capitalize()}!')