# F - разность максимального и минимального натуральных делителей целого числа, не считая единицы и самого числа.
# Если нету таких делителей, то считаем значение F = 0
# Напишите программу, которая перебирает целые числа >850000, в порядке возрастания и ищет среди них такие,
# для которых значение F != 0 и F % 13 == 0. Программа должнай найти и вывести первые 6 таких чисел и значения F для них
a = []
num = 850001
i = 2
f = 0
while len(a) < 6:
    while num % i != 0:
           i += 1
    f = num // i - i
    if i == num:
        f = 0
    i = 2
    if f % 13 == 0 and f != 0:
        a.append([num, f])
    num += 1
    f = 0
print(a)
