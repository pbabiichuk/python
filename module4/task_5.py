print('Задача 5. Модуль числа')

# Создайте программу, которая найдёт модуль очередного числа x. Если число x отрицательное, то она должна перевести его в положительное, а в конце на экране должен быть модуль введённого числа.

# Пример:
# Ввели 5, ответ 5
# Ввели −7, ответ 7

# Подсказка: в некоторых случаях достаточно переприсвоить переменную со знаком минус.

x = int(-5)
a = abs(x)
print('Ввели', x, ',ответ', a)