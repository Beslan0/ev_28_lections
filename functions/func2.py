# str1= "asdvasd vasvsda asdvasdv vsdvasdv vvsadvasdv asdvasdv"

# def get_reversed_string(text):
#     spisok  = text.split() [::-1]

#     return "".join(spisok)

# print(get_reversed_string(str1))    


            
# def sum_of_args(a, b, c = 5, d = 5,): # параметры 
#     return a +b + c + d


# result = sum_of_args(1,2) # аргументы 
# print(result)

# res = sum_of_args
# # print(res, type(res))

# print(res)
# ----------------------------------------------------------
# паозиционные и именновые аргументы

# def printParams(a, b, c):
#     print(a, "is stored in param a")
#     print(b, "is stored in param b")
#     print(c, "is stored in param c")


# printParams(5, 10, 15)
# print()
# printParams(c = 5, b = 10, a = 15)



# def sum_of_args(a, b, c, d): # параметры 
#      return a +b + c + d


# print(sum_of_args(5,10,15,20))# arguments(позиционные аргументы)
# print(sum_of_args(a = 5, b = 10, c = 15, d = 20)) #keyword arguments(именовонные аргуметы)
# print(sum_of_args(5 , 10 , c = 15, d = 20))
# ---------------------------------------------------------------------------------------------------------

# # оператор *
# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)
# -----------------------------------------------
# *args, **kwargs в фукциях

# def printScores(student, *args):
#     print(f"Name of student: {student}")
#     # print(args)
#     print(f"AVG: {sum(args) / len(args)}")
#     for x in args:
#         print("Skore:", x)

# printScores("John Snow", 100, 90,80,70,88,95)

# def printPeTNames(owner, **pets):
#     print(f"Owner name: {owner}")
#     # print(kwargs)
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f"{pet}:", * name)
#         else:
#             print(f"{pet}: {name}")

# printPeTNames("John Snow ", dog = "Pluto", cat = "Garfild", fish= ["nemo", "dori", "batiy" ], turtle = "leonardo")


# def get_some_data(a , b, *args, **kwargs):
#     print("параметры a и b:", a, b)
#     print("аргументы", args)
#     print("именновонные аргументы", kwargs)

# get_some_data(1,2,3,4,5, lang = "Python", car = "BMV")

# def generate_random_string(len_):
#     import string as s
#     import random
#     # print(s.ascii_letters, s.digits, s.punctuation)
#     symbols = s.ascii_letters + s.digits 

#     res = list(random.choice(symbols) for i in range(1, len_)) + list(random.choice(s.punctuation)) 
#     random.shuffle(list(res))
#     return "".join(res)

# print(generate_random_string(15))

  












