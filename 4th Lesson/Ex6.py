# Заполнить массив а случайными числами, отобрать в массив b все числа, меньшие пяти. Вывести оба массива.

from random import *

a = [int(random() * 100) for i in range(20)]
print(a)
b = [i for i in a if i<5]
print(b)
