# Ввести с клавиатуры координаты двух точек (A и B) на
# плоскости (вещественные числы). Вычислить длину отрезка AB
Ax, Ay, Bx, By = map(float, input().split())
print(round(((Ax - Bx) ** 2 + (Ay - By) ** 2) ** 0.5, 2))
