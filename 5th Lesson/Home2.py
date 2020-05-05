# Матрицу размером n заполнить спиралькой
n = int(input())
a = [[0] * n for i in range(n)]


def printMatrix(matrix):
    for row in matrix:
        for x in row:
            print("{:4.0f}".format(x), end="")
        print()


def getNum(s, x, y):  # пришлось скопировать код для получения числа по индексам и размерности из интернета
    x = 2 * x - s + 1  # потому что я не настолько хорош в математики к сожалению
    y = 2 * y - s + 1
    n = max(abs(x), abs(y))
    p = (x + y) / 2
    if x < y:
        p = 2 * n - p
    return s * s - n * n - n + p


a = [[getNum(len(a), i, j) for i in range(len(a))] for j in range(len(a))]
printMatrix(a)
