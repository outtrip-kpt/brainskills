n_card = int(input('Введите количество карт: '))
sum_card = 0
for i in range(1, n_card+1):
    sum_card += i
for i in range(1, n_card):
    print('Введите карту', i, 'из', n_card, ': ', end='')
    while True:
        true_card = int(input())
        if 0 < true_card <= n_card:
            break
        print('Такой карты не было, повторите ввод:')
    sum_card -= true_card
print('Потеренная карта:', sum_card)