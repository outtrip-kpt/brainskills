def list_of_simple(first, second):
    return [i for i in range(first, second + 1) if len([j for j in range(1, i) if i % j == 0]) == 1]


while True:
    n = input('Введите два числа через пробел (диапазон): ').split()
    n = list(map(int, n))
    if len(n) == 2:
        if n[0] < n[1]:
            break
        elif n[0] > n[1]:
            n[0], n[1] = n[1], n[0]
            break
        else:
            print('Пустой диапазон повторите ввод')

print(*list_of_simple(n[0], n[1]))
