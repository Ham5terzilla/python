# Найдите все натуральные числа принадлежащие отрезу [35 000 000; 40 000 000], у которых
# ровно пять различных нечётных делителей (кол-во чётных делителей может быть любым).
# В ответе перечислите найденные числа в порядке возрастания.
# 1 3 5 7 381000
p_list = [i for i in range(3, 381000, 2)]
a = []


def oddness(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return n
    else:
        return oddness(n // 2)


def division(n, *nn):
    if n == 0:
        return None
    if len(nn) == 0:
        nn = [n]
    if n % 2 == 0:
        return division(n // 2, *nn)
    if len(nn) == 5:
        for i in range(len(p_list)):
            if n % p_list[i] == 0:
                return None
        print(nn)
        return nn[0]
    for i in range(len(p_list)):
        if n % p_list[i] == 0:
            if nn.__contains__(p_list[i]):
                return None
            return division(n // p_list[i], *[*nn, p_list[i]])


# for i in range(35000000, 40000001):
#   cnt = 0
#  for j in range(len(p_list)):
#     if cnt

print([oddness(i) for i in range(1000)])
print([j for j in [division(i) for i in range(35000000, 35819660)] if j is not None])
