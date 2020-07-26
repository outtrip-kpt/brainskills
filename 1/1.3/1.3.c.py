day_km = int(input())
end_marafon = int(input())
all_km = day_km
day_count = 1
while all_km < end_marafon:
    day_km += day_km / 10
    all_km += day_km
    day_count += 1
print(day_count)