# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n= a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input('Input n ')) #общее кол-во эл-в
x = int(input('Input a[0] '))
d = int(input('Input d ')) #шаг
print(*range(x, x + d * n, d))



# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint
 
lo, hi = 3, 8
data = [randint(1, 10) for _ in range(20)]
print("Original array:", data, sep='\n')
indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
print("Indexes:", indexes, sep='\n')
result = []
i = len(indexes)
while i :
    i -= 1
    result.append(data.pop(indexes[i]))
print("Remaining elements:", data, sep='\n')
print("Required elements:", result, sep='\n')
