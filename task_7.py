print('Задача 7. Режем число на части')

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

a = int(input('Для входа требуется четырёхзначное число: '))
number_1 = int(a // 1000)
number_2 = int(a % 10)
number_3 = int(a // 100)
number_4 = int(a % 10)
print(number_1)
print(number_2)
print(number_3)
print(number_4)