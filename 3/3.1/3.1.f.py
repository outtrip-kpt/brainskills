def func(n):
    if n == 1:
        return -1
    elif len([i for i in range(1, n) if n % i == 0]) == 1:
        return 1
    else:
        return 0


print(func(int(input())))
