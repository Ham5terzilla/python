# Составить программу для нахождения чисел из интервала [М, N], имеющих наибольшее количество делителей.
M, N = [int(input()) for i in range(2)]
lst_primes = [1, 2]


def getDivs(n):
    lst=[]
    i = 0
    if n > lst_primes[-1]:
        getPrimes(n)
    while n != 1:
        for i in range(1, len(lst_primes)):
            if n % lst_primes[i] == 0:
                n //= lst_primes[i]
                lst.append(lst_primes[i])
                break
    return lst


def getPrimes(n):
    n += 1
    f = 1
    for i in range(lst_primes[-1] + 1, n):
        for j in range(lst_primes[-1] + f, i + 1):
            if [j % lst_primes[i] for i in range(1, len(lst_primes))].__contains__(0):
                f += 1
                break
        else:
            lst_primes.append(i)
            f = 1


cmax = 0
imax = 0
for i in range(M, N+1):
    div_lst = getDivs(i)
    if len(div_lst) > cmax:
        cmax = len(div_lst)
        imax = i

print(imax, getDivs(imax))