row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col = ['1', '2', '3', '4', '5', '6', '7', '8']
row.sort(reverse=True)
ls = []

def list_step(x, y):

    index_x = row.index(x) + 2
    index_y = col.index(y) + 1
    if 0 <= index_x <= 7:
        if 0 <= index_y <= 7:
            ls.append(row[index_x] + col[index_y])
        index_y = col.index(y) - 1
        if 0 <= index_y <= 7:
            ls.append(row[index_x] + col[index_y])
    #-----------------------------------------------------------
    index_x = row.index(x) - 2
    index_y = col.index(y) + 1
    if 0 <= index_x <= 7:
        if 0 <= index_y <= 7:
            ls.append(row[index_x] + col[index_y])
        index_y = col.index(y) - 1
        if 0 <= index_y <= 7:
            ls.append(row[index_x] + col[index_y])
    #-----------------------------------------------------------
    index_y = col.index(y) + 2
    index_x = row.index(x) + 1
    if 0 <= index_y <= 7:
        if 0 <= index_x <= 7:
            ls.append(row[index_x] + col[index_y])
        index_x = row.index(x) - 1
        if 0 <= index_x <= 7:
            ls.append(row[index_x] + col[index_y])
    #-----------------------------------------------------------
    index_y = col.index(y) - 2
    index_x = row.index(x) + 1
    if 0 <= index_y <= 7:
        if 0 <= index_x <= 7:
            ls.append(row[index_x] + col[index_y])
        index_x = row.index(x) - 1
        if 0 <= index_x <= 7:
            ls.append(row[index_x] + col[index_y])


while True:
    print('Введите стартовую позицию фигуры в формате "a1":')
    start = input().lower()
    if start[0] in row and start[1] in col:
        break
    else:
        print('Не верный формат ввода')
while True:
    print('Введите следующую позицию фигуры в формате "a1":')
    stop = input().lower()
    if stop[0] in row and stop[1] in col:
        break
    else:
        print('Не верный формат ввода')

list_step(start[0], start[1])
if stop in ls:
    print('Можно попасть из клетки', start, 'в клетку', stop, 'за один ход')
else:
    print('Из клетки', start, 'в клетку', stop, 'не возможно попасть за один ход')

for i in row:
    for j in col:
        if i+j == start :
            print('∅', end='\t')
        elif i+j == stop:
            print('៙', end='\t')
        elif i+j in ls:
            print('҉', end='\t')
        else:
            print('⋅', end='\t')
    print()
