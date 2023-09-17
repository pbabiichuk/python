a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
num_sum = 0
count = 0
for num in range(a, b + 1):
    if num % 3 == 0:
        num_sum += num
        count += 1
print(f'Cреднее арифметическое всех чисел из отрезка [{a}; {b}], кратных числу 3: {num_sum/count}')
