# S - сумма различных натуральныйх делителей целого числа, являющихся простыми числами, не считая самого числа
# Напишите программу, которая перебирает целые числа >650000, в порядке возрастания и ищет среди них такие,
# для которых значение S оканчивается на цифру 5, вывести 5 таких и значение S
simple = [2, 3, 5]
num = 650001
a = []


def simples(to):
    for i in range(simple[len(simple)-1], to):
        local_cnt = 0
        for j in range(len(simple)):
            if i % simple[j] != 0:
                local_cnt += 1
            else:
                break
        if local_cnt == len(simple):
            simple.append(i)


while len(a) < 50:
    s_list = []
    simples((num//2) + 1)
    for i in range(len(simple)):
        if num % simple[i] == 0:
            s_list.append(simple[i])
        if (num // 2) + 1 < simple[i]:
            break
    S = sum(s_list)
    if S % 10 == 5:
        a.append([num, S])
    num += 1
    S = 0
print(a)
