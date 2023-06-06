# ----------------задача--------------------------------------------
# Задача 30:
# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


# ----------------решение-------------------------------------------
# start = int(input('Введите первый элемент: '))
# step = int(input('Введите разность: '))
# count = int(input('Введите кличество элементов: '))

# array = []
# for i in range(start, (start + (count-1) * step)+1, step):
#     array.append(i)
# print(array)

# --------------конец решени----------------------------------------

# ----------------задача--------------------------------------------
# Задача 32:
# Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума
# и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]

# ----------------решение-------------------------------------------

# array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# min = int(input('Введите минимальное значение: '))
# max = int(input('Введите максимальное значение: '))

# print(f"В массиве: {array}" 
#       f"\n Заданому диапазону от {min} до {max}" 
#       f"\n Принадлежат индексы: ", end='')

# for key, value in enumerate(array):
#     for i in range(min, max + 1):
#         if i == value:
#             print(key, end=' ')


# --------------конец решени----------------------------------------