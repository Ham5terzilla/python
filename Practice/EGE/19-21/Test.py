# constants
multiplayer = 2  # если умножить на константу
increase = 5
end_amount = 100
starting_amount = 95
# end constants


def getNums(num1, num2, depth):
    tmp = []
    if depth > 3:
        return
    for i in range(4):
        numbers = []
        win = False
        if i == 0:
            numbers = [num1, num2 ** 2]
        elif i == 1:
            numbers = [num1, num2 + increase]
        elif i == 2:
            numbers = [num1 ** 2, num2]
        elif i == 3:
            numbers = [num1 + increase, num2]
        if sum(numbers) >= end_amount:
            win = True
        tmp.append({
            "depth": depth,
            "parent": [num1, num2],
            "numbers": numbers,
            "sum": sum(numbers),
            "win": win,
            "child": getNums(*numbers, depth + 1)
        })
    return tmp


a = [getNums(3, i, 1) for i in range(1, starting_amount + 1)]
# Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите минимальный S, когда это возможно
# a[0 - starting_amount][0-4]["child][0-4]
S_list = []
for S in range(len(a)):
    for i in range(4):
        for j in range(4):
            if a[S][i]["win"] == False and a[S][i]["child"][j]["win"]:
                S_list.append(S + 1)
S_list = list(set(S_list))
print(S_list)
# Петя выигрывает вторым ходом. Первым не может. Выиграть должен при любом ходе Вани
S_list = []
for S in range(len(a)):
    for i in range(4):  # Первый ход, Петя 4
        v1win = []
        if not a[S][i]["win"]:  # Если Петя не выиграл первым ходом
            v1win = [a[S][i]["child"][v1]["win"] for v1 in range(4)]  # Список состояний после хода Вани
            if not v1win.__contains__(True):
                p2wins = 0
                for j in range(4):  # итератор второго уровня (Ваня) 16
                    p2win = [a[S][i]["child"][j]["child"][p2]["win"] for p2 in range(4)]
                    if p2win.__contains__(True):
                        p2wins += 1
                if p2wins == 4:
                    S_list.append(S + 1)
S_list = list(set(S_list))
print(S_list)

# У Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети
# У Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом, но ситуация,
# когда Ваня может выиграть первым ходом, реализоваться может
# Найти минимальный S, когда это возможно
S_list = []
# сначала ходит Петя. Петя никак не должен выиграть 1 ходом, варианты где у Пети есть возможность выиграть 1 ходом искл
# Дальше, ходит Ваня. Если Ваня может выиграть 1 ходом, то он выигрывает. Если не может, то он ищет такой ход
# чтобы Петя не имел возможности выиграть дальше
for s in range(len(a)):
    p1win = [a[s][i]["win"] for i in range(4)]  # Выигрыши на 1 ходу, Петя
    if not p1win.__contains__(True):  # Если Петя не выиграл на 1 ходу
        print("s =", s + 1)
        for i in range(4):
            v1win = [a[s][i]["child"][j]["win"] for j in range(4)]
            print(v1win, i + 1)

S_list = list(set(S_list))
print(S_list)
"""b = [getNums(3, s, 1) for s in S_list]
for s in range(len(b)):
    print("\n", s + 1)
    for i in range(4):
        print(f'|->\tnumbers {b[s][i]["numbers"]}'
              f',\tsum {b[s][i]["sum"]}'
              f', win {b[s][i]["win"]}')
        for j in range(4):
            print(f'|\t\tnumbers {b[s][i]["child"][j]["numbers"]}'
                  f',\tsum {b[s][i]["child"][j]["sum"]}'
                  f', win {b[s][i]["child"][j]["win"]}')
            for k in range(4):
                print(f'|\t\t\tnumbers {b[s][i]["child"][j]["child"][k]["numbers"]}'
                      f',\tsum {b[s][i]["child"][j]["child"][k]["sum"]}'
                      f', win {b[s][i]["child"][j]["child"][k]["win"]}')"""




