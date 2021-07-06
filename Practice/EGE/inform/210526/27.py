# Необходимо набрать из каждый пары ровно одно число так, чтобы сумма всех выбранных числе не делилась на 17
# и при этом была максимально возможной.
f = open("3pair.txt", 'r')
f_len = int(f.readline())
a = []
for i in range(f_len):
    j, k, l = map(int, f.readline().split())
    b = [j, k, l]
    b.sort(reverse=True)
    b.append(b[0]-b[1])
    b.append(b[0]-b[2])
    a.append([b[0], b[3], b[4]])
f.close()
print(a)
summa = sum([a[i][0] for i in range(len(a))])
if summa % 17 == 0:
    absolute_min = min(*[a[i][1] for i in range(len(a))], *[a[i][2] for i in range(len(a))])
    summa -= absolute_min
print(summa)