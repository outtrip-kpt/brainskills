def print_mtx(mtx):
    for i in mtx:
        for j in i:
            print('{:<4}'.format(j), end='')
        print()


nm = list(map(int, input('Введите размер матрицы через пробел (строки столбцы): ').split()))

if nm[1] % 2 != 0:
    all_item = ['.' if i % 2 == 0 else '*' for i in range(0, nm[0] * nm[1])]
else:
    all_item = [('.' if i % 2 == 0 else '*') if j % 2 == 0 else ('*' if i % 2 == 0 else '.') for i in range(0, nm[0])
                for j in range(0, nm[1])]

mtx = [[all_item.pop(0) for j in range(1, nm[1] + 1)] for i in range(1, nm[0] + 1)]

print_mtx(mtx)
