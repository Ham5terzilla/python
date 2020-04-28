# Определить, является ли трегуольник со сторонами a,b,c равнобедренным
a, b, c = map(int, input().split())
if a == b or a == c or b == c:
    print("Является")
else:
    print("Не является")
