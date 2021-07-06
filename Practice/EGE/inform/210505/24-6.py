# Текстовый файл (24-варианты 6-14.txt) состоит из неболее чем из 10**6 символов арабских цифр (0-9)
# Определите максимальное кол-во идущих подряд цифр одинаковых цифр

f = open("24 варианты 6-14.txt", 'r')
a = f.read()
f.close()
max_cnt = 0
cur_cnt = 1
for i in range(len(a)):  # от 0 до 10^6
    if a[i] == a[i-1]:   # 123456 121212   a[i] != a[i + 1]
        cur_cnt += 1
    else:
        max_cnt = max(max_cnt, cur_cnt)
        cur_cnt = 1
print(max_cnt)