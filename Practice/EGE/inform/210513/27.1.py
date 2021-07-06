# Необходимо набрать из каждый пары ровно одно число так, чтобы сумма всех выбранных числе не делилась на 31
# и при этом была максимально возможной.
f = open("27v01_B.txt", 'r')
f_len = int(f.readline())
a = []
for i in range(f_len):
    j, k = map(int, f.readline().split())
    a.append([max(j, k), min(j, k), abs(j-k)])
f.close()
print(a)
f_sum = sum([a[i][0] for i in range(len(a))])
print(f_sum)
if f_sum % 31 == 0:
    i_min = 0
    for i in range(len(a)):
        if a[i][2] == max(a[i][2], a[i_min][2]):
            i_min = i
    for i in range(len(a)):
        if a[i][2] == min(a[i][2], a[i_min][2]):  # bool and bool  in a [max, min, difference]
            print(a[i])
            if a[i][2] % 31 != 0:
                i_min = i
    f_sum = f_sum + a[i_min][1] - a[i_min][0]
    print(i_min, a[i_min])
print(f_sum)
