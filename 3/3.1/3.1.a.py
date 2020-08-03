def sum_n(n):
    return sum([int(i) for i in n])


while True:
    try:
        print(sum_n(input()))
    except ValueError:
        print('Введите число')
    else:
        break
