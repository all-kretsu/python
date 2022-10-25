# Передать список в строку

word_list = ['в', '5', 'часов', '17', 'минут',
             'температура', 'воздуха', 'была', '+5', 'градусов']

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

print(word_list)
string_list = ' '.join(word_list)
print(string_list)
