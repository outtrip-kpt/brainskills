with open('doc.txt', 'r', encoding='UTF-8') as f:
    with open('doc1.txt', 'w', encoding='UTF-8') as fw:
        while True:
            line = f.readline()
            if not line:
                break
            print(line.rstrip(), file=fw)