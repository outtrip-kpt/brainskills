whole = 'IXCM'
half = 'VLD'

while True:
    print('Введите число от 1 до 3999')
    s = input()
    if 1 <= int(s) <= 3999:
        break

for indx, i in enumerate(s):
    i = int(i)
    if i == 9:
        print(whole[len(s) - 1 - indx], end='')
        print(whole[len(s) - indx], end='')
    if 6 <= i <= 8:
        r = len(s) - 1 - indx
        print(half[len(s) - 1 - indx], end='')
        for j in range(0, i % 5):
            print(whole[len(s) - 1 - indx], end='')
    if i == 5:
        print(half[len(s) - 1 - indx], end='')
    if i == 4:
        print(whole[len(s) - 1 - indx], end='')
        print(half[len(s) -1 - indx], end='')
    if 1 <= i <= 3:
        for j in range(0, i):
            print(whole[len(s) - 1 - indx], end='')
