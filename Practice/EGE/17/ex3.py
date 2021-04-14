a = [i for i in range(125256, 125331)]
b = []
d = []
cnt = 0
c = 0
for i in range(len(a)):
    for j in range(2, a[i] + 1, 2):
        print(f'{a[i]} % {j} = {a[i]%j}')
        if a[i] % j == 0:
            if cnt > 6:
                d = []
                cnt = 0
                break
            cnt += 1
            d.append(j)
    if cnt == 6:
        b.append(d)
        d = []
        cnt = 0
    else:
        d = []
        cnt = 0
print(b)
