# Найдите все натуральные числа принадлежащие отрезу [35 000 000; 40 000 000], у которых
# ровно пять различных нечётных делителей (кол-во чётных делителей может быть любым).
# В ответе перечислите найденные числа в порядке возрастания.
# 1 3 5 7 381000

from datetime import datetime


p_list = [i for i in range(3, 381000, 2)]
a = []


def oddness(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return n
    else:
        return oddness(n // 2)


#for i in range(35000000, 40000001):
start_time = datetime.now()
for i in range(35000000, 40000001):
    cnt = 0
    i_odd = oddness(i)
    #print(f"Для числа {i} нечётная версия {i_odd}, корень из {i_odd} примерно равен {int(i_odd**0.5) + 1}, операции для него:")
    for j in range(1, int(i_odd**0.5) + 2):
        if cnt >= 5:
            break
        if i_odd % j == 0:
            #print(f"{i_odd} % {j} == 0, текущий счётчик {cnt}, должен стать {cnt + 2}")
            cnt += 2
            if j % 2 == 0:
                cnt -= 1
            if (i_odd // j) % 2 == 0 or i_odd // j == j:
                cnt -= 1
            #print(f"Первое число чётное? {j % 2 == 0}, {i_odd} // {j} == {i_odd // j}, число чётное? {(i_odd // j) % 2 == 0}, равеноство = {i_odd // j == j}, счётчик теперь = {cnt}")
    #print(f"Закончил проверки для {i} с результатом {cnt}")
    if cnt == 5:
        print(i)
print(datetime.now() - start_time)
#start_time = datetime.now()
#for i in range(39037400, 39039449):
#    cnt = 0
#    print(f"Для числа {i} нечётная версия {i}, корень из {i} примерно равен {int(i ** 0.5) + 1}, операции для него:")
#    for j in range(2, int(i ** 0.5) + 2):
#        if cnt >= 5:
#            break
#        if i % j == 0:
#            print(f"{i} % {j} == 0, текущий счётчик {cnt}, должен стать {cnt + 2}")
#            cnt += 2
#            if j % 2 == 0:
#                cnt -= 1
#            if (i // j) % 2 == 0 or i // j == j:
#                cnt -= 1
#            print(f"Первое число чётное? {j % 2 == 0}, {i} // {j} == {i // j}, число чётное? {(i // j) % 2 == 0}, равеноство = {i // j == j}, счётчик теперь = {cnt}")
#    print(f"Закончил проверки для {i} с результатом {cnt}")
#    if cnt == 4:
#        print(f"\n{i}\n")
#print(datetime.now() - start_time)
#print([oddness(i) for i in range(1000)])
#print([j for j in [division(i) for i in range(35000000, 35819660)] if j is not None])
