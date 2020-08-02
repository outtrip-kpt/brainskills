group_d = {i: [] for i in range(1, 60)}
while True:

    print('-------------------------------------------------------------------------')
    print('| Введите через пробел, ФИО студента, номер группы (1-59), средний бал. |')
    print('| Для завершения ввода отправте пустую строку                           |')
    print('-------------------------------------------------------------------------')
    tmp = input().split()

    if len(tmp) == 0:
        break
    try:
        group_d[int(tmp[3])].append(float(tmp[4]))
    except KeyError:
        print('Такой группы не существует, повторите ввод')
    except ValueError:
        print('Средний балл студентя не является числом, повторите ввод')
    except IndexError:
        print('Было введено недостаточное количество данных, повторите ввод')
    else:
        print('''
Добавлен студент: {} {} {}  
из группы: {}  
средний балл: {}
'''
              .format(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]))

for key, val in group_d.items():
    try:
        print(key, sum(val) / len(val))
    except ZeroDivisionError:
        # print(key, 0)
        pass
