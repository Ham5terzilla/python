# Ввести 5 целых чисел, найти максимальное из них
a, b, c, d, e = map(int, input().split())
max = a
if max < b: max = b
if max < c: max = c
if max < d: max = d
if max < e: max = e
print(max)
