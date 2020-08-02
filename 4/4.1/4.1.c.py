with open('doc.txt', 'r', encoding='UTF-8') as f:
    data = f.readlines()

with open('doc_reverse.txt', 'w', encoding='UTF-8') as f:
    for i in data[::-1]:
        print(i.rstrip(), file=f)