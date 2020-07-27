def one_example(first, second):
    return '{} x {} = {:<4}'.format(first, second, first * second)


def line_out(first, second, num_block):
    for i in range(first, second):
        print(one_example(i, num_block), end='\t\t')
    print()


def block(start, over, start_line, over_line):
    for i in range(start, over + 1):
        line_out(start_line, over_line, i)


while True:
    n = input('Введите два числа через пробел (диапазон таблицы): ').split()
    n = list(map(int, n))
    if len(n) == 2:
        if n[0] < n[1]:
            break
        elif n[0] > n[1]:
            n[0], n[1] = n[1], n[0]
            break
        else:
            print('Пустой диапазон повторите ввод')

LEN_RANGE = n[1] - n[0] + 1
COLUMN = int(round(LEN_RANGE ** .5, 0)) if LEN_RANGE % round(LEN_RANGE ** .5, 0) + 1 != 0 else int(
    round(LEN_RANGE ** .5, 0)) + 1

while True:
    number_of_col = input(
        'Введите количество столбцов таблицы (от {} до {}) либо нажмите ENTER (значение по умолчанию - {}): '.format(1,
                                                                                                                     LEN_RANGE,
                                                                                                                     COLUMN))
    if number_of_col == '':
        number_of_col = COLUMN
        break
    elif 1 <= int(number_of_col) <= LEN_RANGE:
        number_of_col = int(number_of_col)
        break
    else:
        print('Невозможное количество столбцов, введите от {} до {}'.format(1, LEN_RANGE))

row = int(LEN_RANGE / number_of_col) if LEN_RANGE % number_of_col == 0 else int(LEN_RANGE // number_of_col + 1)

print()

tmp_start = n[0]
tmp_over = n[0] + number_of_col
while row != 0:
    block(n[0], n[1], tmp_start, tmp_over)
    print()
    tmp_start = tmp_over
    if tmp_start + number_of_col > n[1]:
        tmp_over = tmp_start + (n[1] - tmp_start + 1)
    else:
        tmp_over = tmp_start + number_of_col
    row -= 1
