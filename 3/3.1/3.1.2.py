def Len(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


def square(x1, x2, x3, y1, y2, y3):
    side_a = Len(x1, x2, y1, y2)
    side_b = Len(x2, x3, y2, y3)
    side_c = Len(x1, x3, y1, y3)
    half_perimeter = (side_a + side_b + side_c) * (1 / 2)
    return (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) ** .5


coordinates = []

for i in range(1, 4):
    n = input("Введите координаты {}-ой точки через пробел(х у): ".format(i)).split()
    coordinates.extend(map(int, n))

print('площадь треугольника равна: {:10.6f}'.format(square(*coordinates[::2], *coordinates[1::2])))
