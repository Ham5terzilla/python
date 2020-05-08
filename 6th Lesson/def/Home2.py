# Четыре точки заданы своими координатами X(x1, x2), Y(y1, y2), Z(z1, z2), P(p1, p2). Выяснить, какие из них
# находятся на максимальном расстоянии друг от друга и вывести на экран значение этого расстояния. Вычисление
# расстояния между двумя точками оформить в виде процедуры.
from random import *

X, Y, Z, P = [[int(random() * 100) for i in range(2)] for i in range(4)]


def dist(A, B):
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5


# Конечно, само задание было попроще и надо было просто вывести max, но я решил показывать ещё и между какими
# точками это расстояние. Правда с ньюансом.
pairs = [[dist(i, j), i, j] for i in [X, Y, Z, P] for j in [Y, Z, P]]
max = max([pairs[i][0] for i in range(len(pairs))])
lst = [i for i in [i if i.__contains__(max) else None for i in pairs] if i is not None]
print(lst[0])
