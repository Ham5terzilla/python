# Дана последовательность N целых положительных чисел. Необходимо определить количество пар элементов этой
# последовательности, сумма которых делится на m = 80 и при этом хотя бы один элемент из пары
# больше b = 50.

# Пояснение: Для того, чтобы проверить на условие каждый элемент, мы последовательно проверим каждый с каждым. Например:
# 1 2 3 4 5. Сначал будет проверка пар 12, 13, 14, 15, затем 23, 24, 25, далее 34, 35 и наконец, 45.
# Каждый элемент был в паре с каждым другим элементом ровно 1 раз.
# Затем, для того, чтобы быстрее проверять, мы будем пропускать пары, в которых нету элемента больше 50.


f = open("26-3.txt", "r")
