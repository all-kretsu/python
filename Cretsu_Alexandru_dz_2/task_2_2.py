# Передать список в строку

word_list = ['в', '5', 'часов', '17', 'минут',
             'температура', 'воздуха', 'была', '+5', 'градусов']

"""
for word in word_list:
    word_index = word_list.index(word)
    if word == '5':
        word_list[word_index] = '"05"'
    elif word == '17':
        word_list[word_index] = '"17"'
    elif word == '+5':
        word_list[word_index] = '"+05"'       
"""

# Вариант 2 сложный без списка
for word in word_list:
    word_index = word_list.index(word)
    if word.isdigit() and len(word) == 1:
        word_list[word_index] = '0' + word
    elif '+' in word:
        word = word.replace('+', '0')
        if word.isdigit():
            word = '+' + word
            word_list[word_index] = word
           
'''
# Вариант 3 при помощи отдельного списка
integer_list = []
for numb in integer_list:
    integer_index = integer_list.index(numb)
    if '+' in numb:
        numb = numb.replace('+', '')
        integer_list[integer_index] = numb
        if len(numb) < 2:
            integer_list[integer_index] = '0' + numb
    elif len(numb) < 2:
        integer_list[integer_index] = '0' + numb
'''

print(word_list)
string_list = ' '.join(word_list)
print(string_list)
