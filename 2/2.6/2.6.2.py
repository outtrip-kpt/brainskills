n_str = int(input('Введите количество строк: '))
s = []
for _ in range(n_str):
    s += input().split()
res = {i: s.count(i) for i in s}
out = sorted(list(zip(res.values(), res.keys())), reverse=True)
print(sorted([i[1] for indx, i in enumerate(out) if out[indx][0] == out[0][0]])[0])
