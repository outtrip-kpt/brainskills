n = True
temp_count = 1
temp_n = None
temp_n_max = None
temp_count_max = 0
while n:
    n = int(input())
    if temp_n == n:
        temp_count += 1
    elif temp_count > 1:
        if temp_count > temp_count_max:
            temp_count_max = temp_count
            temp_n_max = temp_n
        temp_count = 1
    temp_n = n
print('число', temp_n_max, 'повторялось подряд в последовательности', temp_count_max, 'раз')



