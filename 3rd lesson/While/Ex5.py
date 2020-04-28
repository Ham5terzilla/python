# Составить программу вывода всех натуральных чисел, меньших n, квадрат суммы цифр которых равен числу m
n = int(input())
m = int(input())
i = 0
j = 0
cur_list = []
while i < n:
    while j < len(str(i)):
        cur_list.append(int(str(i)[j]))
        j += 1
    j = 0
    i += 1
    if sum(cur_list) ** 2 == m: print(*cur_list, sep="")
    cur_list = []
