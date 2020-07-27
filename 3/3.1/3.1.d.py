MAX_DIVISORS = False  # поставить True если число является делителем самого себя


def sum_of_divisors(n):
    return sum([i for i in range(1, n + MAX_DIVISORS) if n % i == 0])


print(sum_of_divisors(int(input())))
