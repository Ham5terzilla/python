# Пользователь вводит 2 числа с клавиатуры. Вывести yes если они отличаются друг от друга на 135, иначе no
# Пользователь вводит номер месяца от 1 до 12, вывести название сезона года.
# Пользователь вводит кол-во месяцев и лет. Вывести на экран кол-во дней за это время. Считать что в месяце 29 дней
a, b, m, month, year = map(int, input().split())
###########
if abs(a - b) == 135: print("Yes")
else: print("No")
###########
if m == 1 or m == 2 or m == 12: print("Зима")
if 3 <= m < 6: print("Весна")
if 6 <= m < 9: print("Лето")
if 9 <= m < 12: print("Осень")
###########
print((year * 12 + month) * 29)
