from random import choice


def delete_file(f):
    with open(f, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        print(data)

    with open(f, 'w', encoding='UTF-8') as file:
        for i in data:
            print('Исходная строка:')
            print(i.rstrip())
            print('Измененная строка:')
            print(i.rstrip().replace('+', '').replace('-', ''))
            print('--------------------------------------------------------------------------------------')
            print(i.rstrip().replace('+', '').replace('-', ''), file=file)

# генерация случайного набора символов
with open('test_file.txt', 'w', encoding='UTF-8') as f:
    print(''.join([choice([*[chr(i) for i in range(33, 65)], chr(10)]) for _ in range(1, 10000)]), file=f)

delete_file('test_file.txt')
