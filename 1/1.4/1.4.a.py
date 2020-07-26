a = int(input())
b = int(input())

while a != 0 and b != 0:
    if a > b:
        print(b, end=' ')
        a -= b
    elif b > a:
        print(a, end=' ')
        b -= a
    else:
        print(a)
        break