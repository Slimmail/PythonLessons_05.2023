# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = int(input("Введите число: "))
# finish_num = 0
# while number > 0 :
#     temp = number % 10
#     number //= 10
#     finish_num = finish_num + temp
# print(finish_num)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10


# boats = int(input("Введите число журавликов: "))
# if boats % 3 == 0 and (boats / 3) % 2 == 0 :
#     temp = boats // 3
#     katya = boats // 3 * 2
#     petr = temp // 2
#     sergey = temp // 2
#     print(petr, katya, sergey)
# else : print("Нет решения")


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.



# ticket_num = int(input("Введите номер билета: "))

# if ticket_num >= 100000 :
#     ticket_num = str(ticket_num)
#     if ticket_num[0] + ticket_num[1] + ticket_num[2] == ticket_num[-1] + ticket_num[-2] + ticket_num[-3] :
#         print(ticket_num + ' -> Yes')
# else : 
#     ticket_num = str(ticket_num)
#     print(ticket_num + ' -> No')



# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no





