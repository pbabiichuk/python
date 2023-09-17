# numbers = []
# for num in range(11):
#     check_num = num + num + num
#     if check_num / 3 == num and check_num > 10:
#         numbers.append(check_num)
# print(f'Список замечательных чисел: {numbers}')

for num in range(10,100):
    if num // 10 * num % 10 * 3 == num:
        print(num)
