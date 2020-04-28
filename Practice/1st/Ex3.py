# Таблица умножения чисел [a,b] на [c,d]
a, b, c, d = [int(input()) for i in range(4)]  # выполняет ввод 4-х чисел. На каждый i выполняется int(input())
print('', *range(c, d + 1), sep="\t")  # Звёздочка распоковывает range(x,y) в print. sep="\t" делает чтобы была
# табуляция
for i in range(a, b + 1):
    print(i, end='\t')  # end='\t' значит что в конце будет не новая строка, а табуляция
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()
