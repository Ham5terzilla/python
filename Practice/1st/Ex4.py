# Среднее арифметическое всех чисел кратных 3 в промежутке [a,b]
a, b = [int(input()) for i in range(2)]
l_list = [i for i in range(a, b + 1) if i % 3 == 0]
s = sum(l_list)
print(s / len(l_list))
