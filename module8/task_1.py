print('Задача 1. Космическая еда')

# Ваш космический корабль потерпел крушение на пустынной планете. Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки. Из прошлого опыта вы знаете, что если будете экономно питаться, то у вас будет уходить по четыре килограмма гречки в месяц.

# Чтобы прикинуть гречневый бюджет, вы решили написать программу, которая выведет информацию о том, сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее, пока она не закончится. Используйте цикл for.

food = 100
for amount in range(1, food, 1):
    food -= 4
    print(f'Через {amount} месяц(а) останется {food} кг гречки')
    if food <= 0:
        break