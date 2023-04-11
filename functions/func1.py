# найти квадрат куб  рузультат деление на 100
# num1 = 5 
# -> {"2": 25, "3": 125, "100": 0.05 }


# num1 = 5
# num2 = 16
# num3 = 28
# num4 = 1154
# num5 = 31



# def operations(num):
#     print({"num": num, "2": num ** 2, "3": num ** 3, "100": num / 0.05 })

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)
# ---------------------------------------------------------

# функция это именнованая часть прогрпммы еоторач содержит в себе определнный набор инструкциий 
# и может вызыватся в лругих часях программы столько раз  сколько угодно 


# def name_of_func(<a, b> # параметры ):
    # <body># код какая то логика котопя будет лавать конечный результат
    # <return> # операторы которые помогает вернуть результат

# name_of_func(5, 6 #аргументы )


# параметры функции это переменыые данные пользователя и хранить в себе эти данные 


# это у нас данные которые мы передаем в функцию в моменте вызова


# ls = [1,2,3,4,5]
# str1 = "Hello world s vami kani i John Snow!"


# def our_len(obj):
#     i = 0
#     print(obj)
#     for x in obj:
#         i += 1
#     print(f"resilt: {i}")


# our_len(ls)
# our_len(str1)





# def get_persenage(money, periud):
#     if money < 30000:
#         raise ValueError("вложить иожео бодее 30000")
#     if periud < 3:
#         raise ValueError("период должен быть не менее 3 лет")
#     year = 0

#     while year < periud:
#         money += money * 0.1
#         year +=1
#     return money

# try:
#     money = float(input("vvedite summu vlojeniy: "))
#     periud = int(input("vvedite periud: "))
#     print(get_persenage(money, periud))
# except:
#     print("nepravilnyi vvod")




# def isEven(obj):
#     # if obj % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     return True if obj % 2 == 0 else False 


# result = isEven(6)
# print(result)
# print(isEven(5))



# def isEven(num: int) -> bool:
#     "our function returns True or False while cheking number for even number"
#     return True if num % 2 == 0 else False 
# print(isEven(5))
# print(isEven(6))


# try:
#     n = int(input("vvedite chislo: "))
# except ValueError:
#     print("Invalid number")
# else:
#     dict_ = {x: x ** 2 for x in range(1, 501) if x % n == 0}
#     print(dict_)



    
