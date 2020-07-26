s = input()
print('*'.join(s))

for indx, i in enumerate(s):
    print(i, end='')
    if indx != len(s)-1:
        print('*', end='')
