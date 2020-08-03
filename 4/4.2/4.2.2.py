def print_mtx(mtx):
    for i in mtx:
        for j in i:
            print('{:<4}'.format(j), end='')
        print()


def next_course():
    global course
    course += 1
    if course == 5:
        course = 1


def fill_cell(row, col):
    if mtx[row][col] == 0:
        mtx[row][col] = all_int.pop()


course = 1
nm = list(map(int, input('Введите размер матрицы через пробел (строки столбцы): ').split()))
mtx = [[0 for j in range(0, nm[1])] for i in range(0, nm[0])]
all_int = sorted([i for i in range(1, int(nm[0]) * int(nm[1]) + 1)], reverse=True)
cur_row = 0
cur_col = 0

while all_int:
    fill_cell(cur_row, cur_col)
    if course == 1:
        try:
            if cur_col + 1 > nm[1] or mtx[cur_row][cur_col + 1] != 0:
                next_course()
            else:
                cur_col += 1
        except IndexError:
            next_course()
    if course == 2:
        try:
            if cur_row + 1 > nm[0] or mtx[cur_row + 1][cur_col] != 0:
                next_course()
            else:
                cur_row += 1
        except IndexError:
            next_course()
    if course == 3:
        try:
            if cur_col - 1 < 0 or mtx[cur_row][cur_col - 1] != 0:
                next_course()
            else:
                cur_col -= 1
        except IndexError:
            next_course()
    if course == 4:
        try:
            if cur_row - 1 < 0 or mtx[cur_row - 1][cur_col] != 0:
                next_course()
            else:
                cur_row -= 1
        except IndexError:
            next_course()

print_mtx(mtx)
