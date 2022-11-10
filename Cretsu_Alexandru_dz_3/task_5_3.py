from random import shuffle

# Урок 3, задание 5, создание генератора шуток.


# списки со словами
nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
verbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'мягкий', 'зеленый', 'утопичный', 'яркий']


# функция с совмещением списков в предложения
def get_jokes(number):
    while number != 0:
        # смешивание списков
        shuffle(nouns), shuffle(verbs), shuffle(adjectives)
        # объединение списков
        zip_words = list(zip(nouns, verbs, adjectives))
        # преобразование в строку и вывод
        print(' '.join(zip_words[0]))
        number -= 1


get_jokes(4)
