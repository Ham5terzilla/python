# Вычисление квадратного корня
from math import *

a, b, c = [float(input()) for i in range(3)]
D = b ** 2 - 4 * a * c
print("D=\t", D)
if D > 0:
    print(round((-b + sqrt(D)) / (2 * a), 3), round((-b + sqrt(D)) / (2 * a), 3), sep="\t")
else:
    print("RIP")
