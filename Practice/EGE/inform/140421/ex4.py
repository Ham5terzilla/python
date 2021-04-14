# F(n) = 1 при n = 1
# F(n) = 2 при n = 2
# F(N) = F(n - 2) + F(3) + n, если n > 2 и n % 2 == 0
# F(n) = F(n - 1) + F(2) + n - 1, если N > 2 и n % 2 == 1
# F(47) - ?
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2 and n % 2 == 0:
        return F(n - 2) + F(3) + n
    if n > 2 and n % 2 == 1:
        return F(n - 1) + F(2) + n - 1


print(F(47))
