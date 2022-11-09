import random

# Урок 3, задание 5, создание генератора шуток.


# списки со словами
nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
verbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'мягкий', 'зеленый', 'утопичный', 'яркий']


# функция с совмещением списков в предложения
def get_jokes(n, v, a):
    random.shuffle(n)
    random.shuffle(v)
    random.shuffle(a)
    zip_words = list(zip(n, v, a))
    print(zip_words)

get_jokes(nouns, verbs, adjectives)