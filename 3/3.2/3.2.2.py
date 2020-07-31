def mean_of_args(*args):
    return sum([i for i in args]) / len(args)


n = list(map(int, input().split()))

print(mean_of_args(*n))
