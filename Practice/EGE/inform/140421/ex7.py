def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n/2)
    if n % 2 == 1:
        return 1 + f(n - 1)


n = 0
while f(n) != 11:
    n += 1
print(n)