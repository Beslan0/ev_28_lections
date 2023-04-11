# Обдость видимости и пространство имен
#  техгология которая определяет контеккст имени (переменные), в рамках которого мы можем ее использовать

# built-ins(встроенные облость видимолсти) -> print, len, max

# global(глобольная) -> область одного файла 

# enclosed(не локальнная (замкнутая), nonlocal )
# local(локальная) -> область внутри одной функции

# x = 200

# def myFunc():
#     print(x)
#     a = 300
#     print(a)

# myFunc()
# # print(a)
# print(x)


# a = 10 # global
# print # builit-in
# def hello(): # global

#     a = "Hello World" # local
#     print(a, "local inside in func!")

# hello()
# print(a, "global")

# # LEGB - local enclosed global built-in
#  -----------------------------------------------------------------

# Enclosed
# замкнутое простроанство имен - локальное пространство у которого есть внутрнее(вложенная) локальное пространство


# x = "global"
# print(x)

# def enclosed(): # global
#     x = "enclosed"
#     def local(): # local 
#         x = "local"
#         print(x)
#     print(x)
#     local()
#     print(x)

# enclosed()
# print(x)

# a = 5
# def func():
#     print(a)
# func()

# global -> позволяет изментять знаячение переменной находясь внутри локальной области
# nonlocal -> позволяет измениять значения не локальной (замкнутой) переменой находясь внутри локальной области

# var = 100
# def increment(): # LEGB
#     global var 
#     var += 1 # var = var + 1

# print(var)
# increment()
# print(var) 
# increment()
# increment()
# increment()
# increment()
# print(var)    

# def counter():
#     num = 0
#     def increment():
#         nonlocal num 
#         num += 1
#         return num
#     return increment
# print(counter())    

# c = counter() # 
# print(c())

# print(c())
# print(c())
# print(c())
# print(c())
# print(c())

# print(dir(__builtins__))
# print(len(dir(__builtins__)))

# globals - func которая возврощает все именна внутри глобальной области видимости 
# locals - func  которая возвращает все именно внутри глобальной облости видимости и локальной 

# def counter():
#     num = 0
#     def increment():
#         nonlocal num 
#         num += 1
#         return num
#     return increment
# print(counter())

# def showStats(heroes,mobs):
#     print()
#     print(f"John Snow ты убил: \n\tгероев: {heroes} \n\tмобов:  {mobs}")

# counter_heroes = counter()
# counter_mobs = counter()
# heroes = 0
# mobs = 0
# print("Приветствую вас, король севера  John Snow, в Весторосе!")
# while True:
#     print("Тебе доступны следуюшие дейтсвия: ")
#     print("1-убить героя, 2-убить моба, 3-статистика, 4-выйти из игры")
#     choice = input("Введите что хотите сделать: ")
#     if choice == "1":
#         heroes = counter_heroes()
#         print()
#         print("Вы обезглавили Ланистра!")
#     elif choice == "2":
#         mobs = counter_mobs()
#         print()
#         print("Вы убили белого ходока!")
        
#     elif choice == "3":
#         print()
#         showStats(heroes,mobs)
#     elif choice == "4":
#         print()
#         print("Пока пока ждём ещё раз!")
#         break




