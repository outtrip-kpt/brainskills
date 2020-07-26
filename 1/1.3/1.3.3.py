# non_zero = True  # если последний ноль тоже считается числом последовательности, тогда изменить на False
# res = []
# n = True
# while n:
#     n = int(input())
#     if n == 0 and non_zero is True:
#         break
#     res.append(n)
# res.sort()
# print('Максимальное число последовательности:', res[len(res) - 1])
# print('Минимальное число последовательности:', res[0])
#



non_zero = True  # если последний ноль тоже считается числом последовательности, тогда изменить на False
max = 0
min = 0
n = True
while n:
    n = int(input())
    if min == 0:
        min = n
    if n == 0 and non_zero is True:
        break
    if max < n:
        max = n
    if min > n:
        min = n

print('Максимальное число последовательности:', max)
print('Минимальное число последовательности:', min)
