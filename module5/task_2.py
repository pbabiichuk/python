print('Задача 2. Функция')

# Учитель математики придумывает каждому ученику отдельные функции, которые нужно отобразить на графике и посчитать. Ещё учитель разбирается в программировании, и чтобы не считать вручную эти функции, он написал программу, которая делает работу за него.

# Напишите программу, которая получает от пользователя число X и вычисляет значение функции Y по следующей схеме:


# Напомним, как это работает:
# Если X больше нуля Y = X - 12.
# Если X равных нулю Y равен пяти.
# Если X меньше нуля Y равен квадрату X.

# Пример:
# Введите икс: 0
# Игрек равен 5

# Пример 2:
# Введите икс: -6
# Игрек равен 36


x = int(input('Введите икс: '))
y = 0
if x > 0:
    y = x - 12
elif x == 0:
    y = 5
else:
    y = x * x
print('Игрек равен:', y)