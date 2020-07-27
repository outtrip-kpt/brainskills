def replace_extremes(num):
    return int('9' + str(num)[1:-1] + '0')


while True:
    n = int(input("Введите число больше 9: "))
    if n > 9:
        break

print(replace_extremes(n))
