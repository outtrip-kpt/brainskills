lst = input().split()

# TODO первый вариант решения
lst = lst[::2]

# TODO второй вариант решения
# for i in range(len(lst)-1, -1, -1):
#     if i % 2 == 0:
#         pass
#     else:
#         lst.pop(i)

print(*lst)