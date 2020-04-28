# Написать программу в результате которой выясняется входил ли число 2 в запись целого числа n
n = int(input())
i = 0
f = False
while i < len(str(n)):
    if "2" == str(n)[i]: f = True
    i += 1
print(f)
