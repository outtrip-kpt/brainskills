L = list(map(int, input('Введие через пробел последовательность елементов: ').split()))
L2 = [L[i] for i in range(-1, len(L) - 1)]
print(L2)