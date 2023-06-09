# ----------------задача-------------------------------------------
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# ----------------решение-------------------------------------------

# import os
# os.system('cls')
# import random

# def get_array(num): # генерируем массив случайных чисел по заданному диапазону
#     array = []
#     for number in range(num):
#         array.append(random.randint(0, 20)) # генерируем массив
#     return array


# array_1 = get_array(7)  # дано по условиям задачи
# array_2 = get_array(12)  # дано по условиям задачи

# print(f'Первый получившийся набор для сравнения: {array_1}')
# print(f'Второй получившийся набор для сравнения: {array_2}')

# array_1_fresh = set(array_1) # убираем повторения
# array_2_fresh = set(array_2) # убираем повторения

# x = list(array_1_fresh.intersection(array_2_fresh)) # получаем пересекающиея элементы множеств
# print(f'Числа, которые встречаются в обоих наборах по мере возрастания: {sorted(x)}')

# --------------конец решени-------------------------------------------

# ----------------задача-------------------------------------------
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

# ----------------решение-------------------------------------------

# import os
# os.system('cls')
# import random

# def get_array(num): # генерируем массив случайных чисел по заданному диапазону
#     array = []
#     for number in range(num):
#         array.append(random.randint(0, 10)) # генерируем массив
#     return array

# def get_max_sum(array):
#         sum_max = array[0] + array[-1] + array[-2]
#         for i in range(0, len(array) -1):
#                 temp = array[i - 1] + array[i] + array[i + 1]
#                 if sum_max < temp:
#                         sum_max = temp
#         return sum_max


# x = int(input('Введите длину поля: '))

# plant = get_array(x) # поле дано по условиям задачи

# grab_max = get_max_sum(plant)

# print(f'В имеющемся поле {plant}')
# print(f'максимальное число ягод, которое может собрать' 
#       f'за один заход собирающий модуль равно: {grab_max}')




# --------------конец решени-------------------------------------------