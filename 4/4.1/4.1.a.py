n = input('Введите числа через пробел: ').split()
with open('list1.txt', 'w', encoding='UTF-8') as f:
    print(' '.join(n), file=f)

with open('list1.txt', 'r', encoding='UTF-8') as fr:
    with open('list2.txt', 'w', encoding='UTF-8') as fw:
        print(' '.join(fr.read().strip().split()[1::2]), file=fw)
