import math

coord_x = int(input('Введите координату x: '))
coord_y = int(input('Введите координату y: '))
coord_x1 = int(input('Введите координату x1: '))
coord_y1 = int(input('Введите координату y1: '))
coord_dist = ((coord_x1 - coord_x) ** 2) + ((coord_y1 - coord_y) ** 2)
sqrt_dist = math.sqrt(coord_dist)
print(f"Расстояние между точками: {sqrt_dist:.2f}")
