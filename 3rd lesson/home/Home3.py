# Найти максимальный элемент численного массива и поменять его местами с минимальным.
from random import *

lst = [int(random() * 2000 - 1000) for i in range(int(input()))]
print(*lst)
imax = 0
imin = 0
for i in range(len(lst)):
    if lst[imin] > lst[i]: imin = i
    if lst[imax] < lst[i]: imax = i
print(lst[imin], lst[imax])
lst[imin] += lst[imax]
lst[imax] = lst[imin] - lst[imax]
lst[imin] -= lst[imax]
print(lst[imin], lst[imax])
