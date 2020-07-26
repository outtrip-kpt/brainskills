
non_zero = True  # если последний ноль тоже считается числом последовательности, тогда изменить на False
count = 0
res = 0
n = True
while n:
    n = int(input())
    count += 1
    res += n
if count - non_zero:
   print(res/(count - non_zero))
else:
    print('0')