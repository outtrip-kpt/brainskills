def minus_extreme(num):
    return int(str(num)[1:-1])


while True:
    n = int(input("Введите число больше 99: "))
    if n > 99:
        break

print(minus_extreme(n))
