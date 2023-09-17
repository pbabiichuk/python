print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

numbers = []
value = 0
count = 0
for item in range(3):
    numbers.append(int(input(f'Введите {item + 1} число: ')))
for el in range(numbers[0], numbers[1] + 1):
    if el % numbers[2] == 0:
        value += el
        count += 1
print(f'Cреднее арифметическое всех чисел из отрезка [{numbers[0]}; {numbers[1]}], кратных числу {numbers[2]}: {value / count}')