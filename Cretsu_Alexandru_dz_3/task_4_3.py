"""Задание 4, урок 3, создание словаря
с ключами: первыми буквами фамилий и значениями: словарями
содержащие ключи: первых букв имен, значения: имена"""

n_s_base = {}
name_dict = {}


def thesaurus_adv(*names):
    n_s_lst = list(x.split() for x in names)
    for pers in n_s_lst:
        for y in pers:
            n_list = list(x.split()[0] for x in n_s_lst)
            s_map_list = list(filter(lambda x: x[-1] == y[-1], pers))
            name_dict[y[0]] = s_map_list

    print(n_s_lst)
    print(name_dict)


thesaurus_adv('Ivan Petrov', 'Joshua Lacremonti',
              'Verner Corsu', 'Boris Vilnew')
