
# Задание 3, урок 3, создание словаря с ключами-буквами и именами-значениями.

n_base = {}


def thesaurus(*name):
    for pers in name:
        person_lst = list(filter(lambda x: x[0] == pers[0], name))
        n_base[pers[0]] = list(sorted(person_lst))


thesaurus('alex', 'artemis', 'alexey', 'boris', 'cecilia', 'dimitry', 'doctur')

print(n_base)
