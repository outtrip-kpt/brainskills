def print_mtx(mtx):
    for i in mtx:
        for j in i:
            print('{:<4}'.format(j), end='')
        print()


def enter_mtx():
    while True:
        try:
            mtx = [[int(input('Значение ячейки [{} Х {}]: '.format(i, j))) for j in range(1, nm[1] + 1)] for i in
                   range(1, nm[0] + 1)]
        except ValueError:
            print('Неверный ввод. Повторите сначала')
        else:
            break
    return mtx


def sub_mtx(first, second):
    return [[first[i][j] - second[i][j] for j in range(0, nm[1])] for i in range(0, nm[0])]


nm = list(map(int, input('Введите размер матрицы через пробел (строки столбцы): ').split()))

print('Введите значения первой матрицы')
mtx_1 = enter_mtx()

print('Введите значения второй матрицы')
mtx_2 = enter_mtx()

print('==========[ матрица №1 ]==========')
print_mtx(mtx_1)
print('==========[ матрица №2 ]==========')
print_mtx(mtx_2)
print('=======[ вычитание матриц ]=======')
print_mtx(sub_mtx(mtx_1, mtx_2))