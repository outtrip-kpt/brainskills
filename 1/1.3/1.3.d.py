fb1 = 1
fb2 = 1
fb = [fb1]
n = int(input())
if n == 0:
    print(0)
else:
    for i in range(1, n):
        fb_sum = fb1 + fb2
        fb1 = fb2
        fb.append(fb1)
        fb2 = fb_sum
        if i == n:
            fb.append(fb2)

print(*fb)
