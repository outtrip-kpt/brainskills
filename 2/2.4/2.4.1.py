L = list(map(int, input('Введие через пробел последовательность елементов: ').split()))
n = int(input('Ведите число: '))

res = [indx for indx, i in enumerate(L) if i == n]
print(res)
