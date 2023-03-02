# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def power(A, B):
    if (B == 1):
        return (A)
    if (B != 1):
        return (A * power(A, B - 1))
A = int(input("Введите число: "))
B = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(A, B))


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    else:
        return a
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))     
print(sum(a, b))
