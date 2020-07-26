L = list(map(int, input('Введие через пробел последовательность чисел: ').split()))
res = set()
for i in L:
    if i in res:
        print(i, 'NO')
    else:
        res.add(i)
        print(i, 'YES')