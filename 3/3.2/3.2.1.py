def min_max():
    min_n = None
    max_n = None
    while True:
        n = int(input())
        if n == 0:
            return min_n, max_n
        if min_n is None:
            min_n = n
        if max_n is None:
            max_n = n
        if max_n < n:
            max_n = n
        if min_n > n:
            min_n = n

print(*min_max())