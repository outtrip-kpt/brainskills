
n = int(input())
res_fact = 1
cnt = 1
while n >= res_fact or n == 0:
    res_fact *= cnt
    cnt += 1
    if n == res_fact or n == 0:
        print(n, 'является факториалом числа', cnt-1)
        break
else:
    print(n, 'не является факториалом какого-либо числа')
