ls = []


def pi_n(n):
    res = 0
    for i in range(1, n*2, 2):
        ls.append(4/i)
        if len(ls) % 2 == 0:
            res -= ls[len(ls)-1]
        else:
            res += ls[len(ls)-1]
    return res


print(pi_n(10))
