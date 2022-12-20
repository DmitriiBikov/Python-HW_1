# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/

# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099


x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1)) ** 0.5:.3f}")
