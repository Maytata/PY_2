# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# from random import randint
# n = int(input(": "))
# lst = [randint(-5, 5) for _ in range(n)]
# k = 0
# i = 0
# for i in range(len(lst)-1):
#     if lst[0] != lst[i+1]:
#         k = k+1
# print(lst)
# print(k)


# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально

# lst = [1, 2, 3, 4, 5]
# k = int(input(": "))
#
# for i in range(k):
#     lst.insert(0, lst.pop())
# print(lst)
#
# #чтобы удалил что нужно
# for i in lst:
#     if i == 1:
#         lst.remove(i)
# print(lst)


# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# slov = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": " S005 "}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# ltn = []
# for dict in slov:
#     for v in dict.values():
#         ltn.append(v.strip())
# ltn = set(ltn)
# print(ltn)


# Задача №23. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
#
# from random import randint
# n = int(input(": "))
# lst = [randint(-5, 5) for _ in range(n)]
# a = 0
# i = 0
# print(lst)
# for i in range(len(lst)-1):
#     if lst[i] < lst[i+1]:
#         a = a+1
# print(a)