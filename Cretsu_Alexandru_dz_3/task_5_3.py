from random import shuffle

# Урок 3, задание 5, создание генератора шуток.


# списки со словами
nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
verbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'мягкий', 'зеленый', 'утопичный', 'яркий']


# функция с совмещением списков в предложения
def get_jokes(n, v, a):
    # смешивание списков
    shuffle(n), shuffle(v), shuffle(a)

    # объединение списков и преобразование в строку
    zip_words = list(zip(n, v, a))
    x = list(' '.join(x) for x in zip_words)
    print(x)


get_jokes(nouns, verbs, adjectives)
