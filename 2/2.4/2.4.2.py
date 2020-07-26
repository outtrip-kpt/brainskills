L = list(map(int, input('Введие через пробел последовательность елементов: ').split()))
print(L, '-> ', end= '')

for i in range(1, len(L), 2):
    tmp = L[i-1]
    L[i-1] = L[i]
    L[i] = tmp
print(L)