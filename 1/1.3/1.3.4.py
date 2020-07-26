# res = set()
# n = True
# while n:
#     n = int(input())
#     res.add(n)
# res = list(res)
# res.sort(reverse=True)
# print(res[1])

n = True
max_first = int(input())
max_second = int(input())
if max_first < max_second:
    tmp = max_first
    max_first = max_second
    max_second = tmp
while n:
    n = int(input())
    if n == 0:
        break
    if n > max_first:
        tmp = max_first
        max_first = n
        if tmp > max_second:
            max_second = tmp

    if max_first > n > max_second:
        max_second = n
print('Второй по величине элемент', max_second)
