def search_all(s_el, elem, lst):
    for i in lst:
        if elem in lst[i]:
            all_element[s_el] += 1
            search_all(s_el, i, lst)

all_element = {}
tree = {}
n = int(input())
for _ in range(1, n):
    temp = input().split()
    if temp[1] in tree:
        tree[temp[1]].append(temp[0])
    else:
        tree[temp[1]] = [temp[0]]
    all_element[temp[0]] = 0
    all_element[temp[1]] = 0

for i in all_element:
    search_all(i, i, tree)

for i in sorted(list(zip(all_element.keys(), all_element.values()))):
    print(*i)
