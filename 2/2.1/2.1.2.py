s = input()
s1 = s.replace('1', 'one')
print(s1)

s2 = None
for i in s:
    if i == '1':
        if s2 is None:
            s2 = 'one'
        else:
            s2 += 'one'
    else:
        if s2 is None:
            s2 = i
        else:
            s2 += i
print(s2)
