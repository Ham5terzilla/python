# Задана квадратная матрица. Переставить строку с максимальным элементом на главной диагонали со строкой с заданным
# номером m.
from random import *


def printMatrix(matrix):
    for row in matrix:
        for x in row:
            print("{:4d}".format(x), end="")
        print()


a_len = int(input())
a_m = int(input()) - 1  # по ленности не стал делать защиту от дурака. Индекс должен быть >=1 и <=a_len

a = [[int(random() * 100) for i in range(a_len)] for i in range(a_len)]
printMatrix(a)  # Вывод первоначальной матрицы
a_dmax = max([a[i][i] for i in range(len(a))])  # Поиск максимального элемента диагонали
# Поиск строки содержащей максимальный элемент диагонали
a_rowdmax = [a.index(i) for i in a if a[a.index(i)].__contains__(a_dmax)][0]
# PS: Можно было сразу найти строку содержащую максимальный элемент диагонали используя одну строку кода
# но это такой изврат
# PPS: В a_rowdmax изначально записываются номера всех строк содержащих максимальный элемент, поэтому я беру первую
# с помощью [expr][0]
print(f'Максимальный элемент главной диагонали:\t{a_dmax}\nСодержится в строке номер:\t{a_rowdmax+1}')
if a_rowdmax == a_m:
    pass
else:
    a.insert(a_rowdmax, a.pop(a_m))
    a.insert(a_m, a.pop(a_rowdmax+1))
printMatrix(a)

