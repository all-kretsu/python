# Задание 1/2, урок 3, перевод слов.

numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
           'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
           'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


# numb = input('Insert here: ')


# Фунция перевода входящих значений
def num_translate(word):
    for eng in numbers:
        if word == eng:
            print(numbers.setdefault(eng))


# num_translate(numb)


# Дополненная функция с возвратом заглавной буквы
def num_translate_adv(word):
    num_translate(word)
    for eng in numbers:
        if word == eng.capitalize():
            print(numbers.setdefault(eng).capitalize())
