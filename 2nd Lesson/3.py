#Ввести три целых числа, найти максимальное из них
a,b,c=map(int,input().split())
#print(max(a,b,c))
if a>b :
    max = a
else:
    max = b
if max<c :
    max = c
print(max)