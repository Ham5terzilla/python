# Организовать беспрерывный ввод чисел с клавиатуры пока пользователь не введёт 0. После ввода нуля
# показать на экран количество чисел, которые были введены, их общую сумму и среднее арифметическое.
s_list = [1]
i = 0
while s_list[i] != 0:
    s_list.append(int(input()))
    i += 1
del s_list[0]
print(*s_list, sep="\t")
print(len(s_list), sum(s_list), sum(s_list) / len(s_list), sep="\t")
########## Использование list.append, .extend и .insert
print()
test_list = ["aa", "bbbb"]
print(test_list)
test_list.append(34)
print(test_list)
test_list.extend(s_list)
print(test_list)
test_list.insert(10, 'Дополнительный элемент')
print(test_list)
