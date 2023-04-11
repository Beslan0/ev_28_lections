# while <expession>
# <body>


# i = 0

# while i < 10:
#     i += 1
#     print(f"Цикл сработал {i} раз!")

# ls = list(range(1, 51))
# print(ls.reverse())
# while ls:
#     print(ls.pop())

# name1 = ""

# name2 = ""

# i = 0

# while name1.lower() != "johne" and name2.lower() != "raychel":
#     name1 = input("vvedite imy1:")
#     name2 = input("vvedite imy2:")  
#     print()
    
#     if i >=5:
#         print("цикл остановлен")
#         break
#     i += 1
# else:
#     print("Ты угадал")


# user = {"username": "JohneSnow", "password": "ilovepython123"}
# i = 3
# # password  = None


# while password := user["password"]: 
#     # password = input(f"{user['username']} vvedite parol\': ")
#     i -= 1
    
#     if i == 0:
#         print("vy zablokirivany!!!")
#         break
    

# else:
#     print(f"{user['username']}vy uspesho zashli v sistemu")

# for <variable> in <iterable object>:
    # body

# list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]

# i = iter(list_)

# print(i)

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# import random

# ls = []
# for x in range(1,101):
#     ls.append(random.randint(1,50))

# print(len(ls))
# ls = set(ls)
# ls = list(ls)
# print(ls)
# print(len(ls))


# ls = ["Tirion" , "bilal", "john", "sansa", "jamie", "eddart"]

# for x in ls:
#     if x == "bilal":
#         continue
#     print(f"Hello Mr/mrs {x}")
    
# i = 0

# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
    

# число 100

# 1, 2, 4, 5, 10, 20, 25, 50, 100

# num = 1_000_000_000
# res = []

# for x in range(1, int(num ** 0.5) + 1):
#     if num % x == 0:
#         res.extend({x, num // x})

# res.sort()
# print(res)


# dict_ = {"Мурату": 24, "Эржану": 21, "Карине": 24, "Алтынай": 17, "Айбеку": 16 }


# if  dict_.values > 17:
#   print("вы не прошли")
# else:
#   print("вы прошли")



# dict_ = {"apple": 14, "orange": 25, "banana": 18 }

# dict_["apple"]


# print(dict_)

# Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. 
# Если он введёт сумму, меньшую чем 0, то запринтите исключение с текстом "Сумма не может быть отрицательной!"
# """

# x = int(input("vvedite sumu: "))
# if x < 0:
#     print("Сумма не может быть отрицательной!")

# x = int(input("vvedite sumu: "))
# if x < 0:
#     print("Сумма не может быть отрицательной!")
# else:
#   print("Сумма успешна")

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# sorted_dict = {}


# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}

# a = ["a"] = 32


# print('Таблица умножения')
 
# for i in range(, 10):
#     for k in range(1, 10):
#         print(f'{i} x {k} = {i * k}\t', end='')
#     print(" ")
    


