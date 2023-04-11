# 1. типпы данных числа -> int, float

# = -> оператор присваивания
# variable (переменная)

# num = 5
# print(num) # 5 
# num = 79 # перепоспределение
# print(num)# 79

# abc -> нижний регистр
# ABC -> верхний регитср

#PEP8
# tomorrow_day = "10.03.2023" # snake case
# tomorrowDay = "10.03.2023" # camel case

# num1 = 5
# num 2 = 15
# result = num1 = num2 
# print("Summa:" result)

# -

# num1 = input("enter the num1:") #-> "5"
#  num2 = input("enter the num2:") # -> "7"

#  num1 = int(num1)
#  num2 = int(num2)

#  print( num1, "-", num2, "=" num1 - num2)

# *

# num1 = int(input("enter the num1:"))
# num2 = int(input("enter the num2:"))
# print( num1, "*", num2, "=" num1 * num2) 

# / and // %
# / - обычное деление
# // - деление без отстака
# % - модульное деленние (получение отстатка от деления)
# num1 = 7
# num2 = 3
# print("/", num1 / num2) # 2.33333
# print("//", num1 // num2) # 2
# print("%", num1 % num2) # 1



# ** -> возведение в степень

# print( 5 ** 2)

# print( 16 ** 55)

# print( 144 ** 0.5) # квадратный корень

# pow - возведение в степень
# pow(num1, num2)

# num1 = 5
# num2 = 10
# print(num1, num2, <mod>)

# print(pow(5, 10))
# print(5 ** 10 % 65)

# a = 5
# b = 2
# res = pow(a, b, 12)
# print(res)


# round() - округление читсла с плавающей точкой

# a = 5.728232
# print(round(a, 2))


# abs() - абсолютное занчение числа -> abs(-5) ->
                                    # |-5| -> 5
#  a = abs(-16)
#  b = abs(15)
#  print(a, b)

# divmod(a, b) -> она выведит два числа б первое число это результат целочисленное деление (//) а на b, а второе это модульное деление 
# res = divmod(5,2)
# print(res)
# print((5 // 2, 5 % 2 ))

# print(9 ** 0.5)

# import math

# a = 5

# # print(round(math.sqrt(a), 2))
# res = math.sqrt(a)
# print(round(res, 2))

# множественное присваивание
# оператор присваивания (=)

#  a = 5 
#  b = 15
#  c = None
#  print("a:" , a, "b;",  b)
 

#  c = a
#  a = b 
#  b = c
#  print("a;" , a, "b;" , b)



#   a, b = b, a

#   print("a;" , a, "b;", b)

# num1, num2, num3 = input("Num1:"), input("Num2:") , input("Num3:")

# print(num1)
# print(num2)
# print(num3)
"""дана переменная  c радиусом окружности найдите периметр и площадь окружности результат выведите в терминал"""

# from math import pi 
# print(pi, type(pi))

# r = int(input("vvedite radius"))
# res_P = 2 * r * pi
# res_S = pi * r * 2

# print("p okruzhnosti:", round (res_S))
# print("S okruzhnosti:", round (res_P))

# from random import randint

# print(randint(1, 10))

# name = input("vedite svoy imy")
# last_name = input("vedite svoy familie")
# num = randint(1_000_00, 9_999_999)
# # print(name, last_name, num)
# res = name + last_name + str(num)
# print(res)

# from random import randint

# num = randint(1, 10)
# print(num)
# i = 0
# while i < 3:
#     guess = int(input("ugadai chisla"))
#     if guess == num: 
#         print(*"you win")
#         break
#     # i = i + 1
#     i += 1 # increment


