# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
n = int(input())
lst = [
        [0 if i < n - j - 1
            else 1 if i == n - j - 1
            else 2
            for i in range(n)]
    for j in range(n)]


def printMatrix(matrix):
    for row in matrix:
        for x in row:
            print("{:3d}".format(x), end="")
        print()


printMatrix(lst)