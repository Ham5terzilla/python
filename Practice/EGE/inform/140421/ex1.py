# Сколько существует различных четырёхзначных чисел,
# записанных в восьмеричной системе счисления,
# в записи которых есть ровно две одинаковые цифры, причём стоящие рядом?

# 4 цифры. XXXX. С 1000 до 7777. Две одинаковые цифры, стоящие рядом, значит формат такой: XXYZ, YXXZ, YZXX.
# Где Y и Z - это любые цифры, не являющиеся цифрой X
a = []
for i in range(1, 8):
    for j in range(8):
        for k in range(8):
            for l in range(8):
                if i == j and i != k and i != l and k != l:
                    a.append([i, j, k, l])
                else:
                    if j == k and j != i and j != l and i != l:
                        a.append([i, j, k, l])
                    else:
                        if k == l and k != i and k != j and i != j:
                            a.append([i, j, k, l])
print(a)
print(len(a))

