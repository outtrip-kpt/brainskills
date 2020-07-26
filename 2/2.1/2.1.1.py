s = input()
indx = int((len(s) / 2)) + len(s) % 2
s1 = s[:indx]
s2 = s[indx:]
print(s2 + s1)
