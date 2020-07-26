s = input().split()
for indx, i in enumerate(s):
    print(i, s[: indx].count(i))
