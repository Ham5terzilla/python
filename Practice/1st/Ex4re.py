# Среднее арифметическое всех чисел кратных 3 в промежутке [a,b]
# ...
l_list = [i for i in range(int(input()), int(input()) + 1) if i % 3 == 0]
print(sum(l_list) / len(l_list))