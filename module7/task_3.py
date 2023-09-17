num = int(input("Введите натуральное число: "))
result = 1
for el in range(1, num + 1):
    result *= el
print(f'Факториал числа {num} = {result}')