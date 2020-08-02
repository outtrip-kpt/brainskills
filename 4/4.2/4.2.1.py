def print_mtx(mtx):
    for i in mtx:
        for j in i:
            print('{:<4}'.format(j), end='')
        print()


nm = list(map(int, input('Введите размер матрицы через пробел (строки столбцы): ').split()))
mtx = [[0 for j in range(0, nm[1])] for i in range(0, nm[0])]
all_int = sorted([i for i in range(1, int(nm[0]) * int(nm[1]) + 1)], reverse=True)

for indx_r, i in enumerate(mtx):
    for indx_c, j in enumerate(i):
        if indx_r % 2 == 0:
            mtx[indx_r][indx_c] = all_int.pop()
        else:
            mtx[indx_r][len(mtx[indx_r]) - indx_c - 1] = all_int.pop()

print_mtx(mtx)
