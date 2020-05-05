# Задача №3 Создать список из 5 элементов, заполнить его случайными числами, вывести его и сумму его элементов
from random import *

lst = [int(random()*2000-1000) for i in range(5)]
print(lst, "\n", sum(lst))
