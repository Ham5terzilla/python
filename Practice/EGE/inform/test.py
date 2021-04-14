s = int(input())
n = 1
i = 0
while s * n < 4096:
    i += 1
    s = s // 2
    n = n * 4
    print(i, "\t", s, "\t", n, "\n")
print(n)