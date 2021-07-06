# XYZ символы
# Определите максимальное кол-во идущих подряд символов, среди которых символ Z встречается не более двух раз
f = open("24 варианты 1-5.txt", 'r')
a = f.read()
f.close()
z_cnt = 0
cur_cnt = 0
cur_cnt_prev1 = 0
cur_cnt_prev2 = 0
max_cnt = 0
for i in range(len(a)):
    cur_cnt += 1
    if a[i] == 'Z':
        z_cnt += 1
        if z_cnt == 2:
            z_cnt = 1
            max_cnt = max(max_cnt, cur_cnt + cur_cnt_prev1 + cur_cnt_prev2 - 4) # ZXXZYYZXXZ -> ZXXZ(4) + ZYYZ(4) + ZXXZ(4) - 4
            cur_cnt_prev2 = cur_cnt_prev1
            cur_cnt_prev1 = cur_cnt
            cur_cnt = 1
print(max_cnt)
