# Определить, существует ли треугольник с длинами сторон a, b, c.
# Если – да, вычислить его площадь по формуле Герона.
a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) * 0.5
    print(round(float(p * (p - a) * (p - b) * (p - c)), 2))
