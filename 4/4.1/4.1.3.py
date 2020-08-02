from random import randint

res = 0
N = 10000
with open('input.txt', 'w', encoding='UTF-8') as f:
    print(''.join(map(str, [randint(0, 9) for i in range(0, N)])), file=f)

with open('input.txt', 'r', encoding='UTF-8') as f:
    for i in f.read().strip():
        res += int(i)

with open('output.txt', 'w', encoding='UTF-8') as f:
    print(res, file=f)
