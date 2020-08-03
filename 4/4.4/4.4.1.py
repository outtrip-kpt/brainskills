def enter_mtx(nm):
    while True:
        try:
            mtx = [[int(input('Значение ячейки [{} Х {}]: '.format(i, j))) for j in range(1, nm[1] + 1)] for i in
                   range(1, nm[0] + 1)]
        except ValueError:
            print('Неверный ввод. Повторите сначала')
        else:
            break
    return mtx


while True:
    try:
        mtx_1 = enter_mtx(list(map(int, input('Введите размер матрицы через пробел (строки столбцы): ').split())))
    except:
        print('Неправильный ввод. Повторите')
    else:
        break

tmp = mtx_1[0][0]
index_j, index_i = 0, 0
for ind_i, i in enumerate(mtx_1):
    for ind_j, j in enumerate(i):
        if j > tmp:
            tmp = j
            index_i = ind_i
            index_j = ind_j


print('Индекс первого вхождения максимального элемента ({}) ->> [{} x {}]'.format(tmp, index_i + 1, index_j + 1))
