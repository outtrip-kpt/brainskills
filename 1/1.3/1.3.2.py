cnt = 0
n = True
while n:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        cnt += 1
print(cnt)