numbers = input("Введите 10 чисел через запятую: ")
int_numbers = numbers.split(",")
count = 0
list_numbers = []
for number in int_numbers:
    if int(number) % 2 == 0 and int(number) > 0:
        count += 1
        list_numbers.append(number)
print(f'Найдено чисел которые одновременно являются одновременно чётными и положительными: {count}, вот они: {list_numbers}')