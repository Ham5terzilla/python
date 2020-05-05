# Создать список из десяти элементов. Заполнить его случайными числами. Заменить все нечетные числа нулями. Вывести
# исходный и получившийся списки.
from random import *

lst = [int(random() * 2000 - 1000) for i in range(10)]
print(lst)
lst = [0 if i % 2 == 1 else i for i in lst]
print(lst)