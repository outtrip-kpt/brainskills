def print_stat(take='you'):
    if take == 'comp':
        print('\t \t \t \t \t \t \t \t \t \t', end='')
    print('Осталость спичек на столе', all_items)
    print('-' * 100)
    if all_items == 1:
        print('****************')
        print('* Вы проиграли *')
        print('****************')
        return exit()

print()
print('='*100)
all_items = 20
comp = 3
print('\t \t \t \t \t \t \t \t \t \t Компьютер взял', comp, 'спичек')
all_items -= comp
print_stat('comp')

while True:
    while True:
        print('Ваш ход')
        you = int(input('Введите количество от 1 до 3: '))
        if 0 < you < 4:
            break
    all_items -= you
    print_stat()
    comp = 4 - you
    all_items -= comp
    print('\t \t \t \t \t \t \t \t \t \t Компьютер взял', comp, 'спичек')
    print_stat('comp')

