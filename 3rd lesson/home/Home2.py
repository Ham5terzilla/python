# Дана строка. Вывести все слова, начинающиеся на букву "а" и слова оканчивающиеся на букву "я".
s = input()
s_list = s.split()
for i in range(len(s_list)):
    if s_list[i][0] == "а":
        if s_list[i][len(s_list[i])-1] == "я":
            print(s_list[i])