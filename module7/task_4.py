students = int(input('Введите число учеников: '))
grades_count = {"отличников": 0, "хорошистов": 0, "троечников": 0}
for student in range(1, students + 1):
    grade = int(input(f'Введите оценку которую получил {student} ученик: '))
    if grade == 5:
        grades_count["отличников"] += 1
    elif grade == 4:
        grades_count["хорошистов"] += 1
    else:
        grades_count["троечников"] += 1

if grades_count["отличников"] == grades_count["хорошистов"] == grades_count["троечников"]:
    print('Сегодня было равное количество отличников, хорошистов и троечников')
else:
    print(f'Сегодня было больше {max(grades_count, key=grades_count.get)}')
