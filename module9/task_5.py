print('Задача 5. Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку. Ему особенно понравилась книга «Преступление и наказание». Паоло решил найти самое длинное слово в этой книге, чтобы сравнить его с аналогом на своём языке.

# Что нужно сделать

# Напишите программу, которая получает на вход текст и находит длину самого длинного слова в нём. Слова в тексте разделяются одним пробелом.

# Пример:

# Введите текст: Меня зовут Пётр.
# Самое длинное слово, букв: 5.

# Введите текст: Меня зовут Василий
# Самое длинное слово, 7 букв

# text = input('Введите текст: ')
# symbolCount = 0
# long_word = []
# for symbol in text:
#     symbolCount += 1
#     if symbol == ' ':
#         print(long_word)
#         long_word.append(symbolCount)
#         symbolCount = 0
# print(long_word)
# print(f'Самое длинное слово, букв: {max(long_word) - 1}.')

text = input('Введите текст: ')
symbolCount = 0
long_word = []
for symbol in text:
    if symbol != ' ':
       symbolCount += 1
    else:
       symbolCount = 0
    if symbol == ' ':
        print(long_word)
        long_word.append(symbolCount)
        symbolCount = 0
print(long_word)
print(f'Самое длинное слово, букв: {max(long_word) - 1}.')