res = 0
with open('doc.txt', 'r', encoding='UTF-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        res += len(line.rstrip())

print(res)
