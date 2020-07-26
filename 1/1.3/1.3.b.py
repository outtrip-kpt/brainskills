n = int(input())
x = 2
res = 1
cnt = -1
while n >= res:
    cnt += 1
    res *= 2
print('Наибольшая целая степень двойки, не превосходящая', n, 'равна', int(res / 2))
print('показатель степени двойки', cnt)