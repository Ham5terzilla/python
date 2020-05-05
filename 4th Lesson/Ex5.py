# Массив, 10 элементов, числа от -100 до 100
# Переставить элементы чтобы >0 были в начале, а <=0 в конце
from random import *

lst = [int(random() * 200 - 100) for i in range(10)]
print(lst)
print([*[i for i in lst if i > 0], *[i for i in lst if i <= 0]])
