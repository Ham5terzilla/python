# Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца,
# в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот,
# у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.
from random import *

a = [[int(random() * 100) for i in range(10)] for i in range(10)]
print(a)
a_max = max([max(a[i]) for i in range(10)])
print(a_max)
for i in a:
    try:
        print(a.index(i), i.index(a_max))
        break
    except ValueError:
        pass