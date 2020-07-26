t = tuple()
print('Введите элементы кортежа, пустая строка конец ввода')
while True:
    n = input()
    if n:
        t += (int(n),)
    else:
        break

for indx, i in enumerate(t):
    if indx != len(t) -1:
        if i > t[indx+1]:
            print('котеж не упорядочен по возростанию')
            break
else:
    print('кортеж упорядочен по возрастанию')