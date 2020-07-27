def minus_extreme(n):
    return int(str(n)[1:-1])


while True:
    n = int(input("Введите число больше 99: "))
    if n > 99:
        break

print(minus_extreme(n))
