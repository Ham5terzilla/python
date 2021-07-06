# F(n) = 1, при n = 1
# F(n) = n + 2 * F(n - 1), когда n % 2 == 0
# F(n) = 2**n + F(n - 2), если n > 1, и n % 2 == 1
# F(16)
def F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + 2 * F(n - 1)
    if n > 1 and n % 2 == 1:
        return 2**n + F(n - 2)


print(F(16))
