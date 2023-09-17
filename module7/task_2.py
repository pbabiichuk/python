total = []
for month in range(12):
    salary_value = int(input(f'Введите размер заработной платы за {month + 1} месяц: '))
    total.append(salary_value)
print(f'Средняя заработная плата за последние 12 месяцев составила {sum(total)/12}')