a = input()
b = input()
try:
    if a.find('.') != -1 or b.find('.') != -1:
        print(float(a) + float(b))
    else:
        print(int(a) + int(b))
except:
    print(a + b)