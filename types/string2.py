# print(dir("5"))
# print(dir(int))
# a = "Hello"
# b = "John"
# # print(a != b)
# # print("abc" == "abc")
# print(a > b)
# print(a < b)
# print("a") # 97 -> 1100001
# print("a" > "b") # 97 > 98
# print("h" > "c") # 104 > 99
# print("hello" > "harry") # true
# print("abc" > "abc") #False

# len - возврощяет кол-во симваолов в строке
# a = "Hello"
# b = "john snow"
# print(len(a) < len(b))
# print(len(a), len(b))
 
# Методы строк
# replace(old, new, [count]) - меняет в строке символы old на new, если вы укажете count, то заменит count раз
# text = "ha ha ha ha"
# result = text.replace("a", "e", 2)
# print(text)
# print(f"result after replace: {result}")

# str1 = "Hello world! My name is John Snow!"
# res = str1.replace("John Snow", "Tirion Lanister")
# print(res)

# strip() - убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = "   Hello   "
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))
# print(dir(str))

# isdigit   -        проверяют 
# isnumeric - ->   состоит ли наша строка
# isdecimal -        полностью из чисел

# num = input("vvedite chislo:")
# print(f"vvedeno chislo?: {num.isdigit()}")
# num = input("vvedite chislo:")
# if num.isdigit():
#     num = int(num)
#     print(f"{num} + 5 = {num + 5 }")
# else:
#     print("vedenno ne choislo")

# text = "/u0034"
# print(text)
# print(text.isnumeric())
# print(text.isdigit)()
# print(text.isdecimal())

# isalnum() - проверяет состоит ли наша строка из чисел и символов латинского алфавита и киррилицы

# str1 = "61a"
# print(str1.isalnum())
# str2 = "56_a"
# print(str2.isalnum())

# isalpha -> состаоит ли наша строка полностью из символов алфавита

# text = "Hello world"
# res = text.replace(" ","")
# print(res)
# print(res.isalpha())

# islower()
# isupper()
# istitle()

# str1 = "Ms. My Name "
# print(str1.islower())
# print(str1.istitle())
# str2 = "RTY UIOP"
# print(str2.isupper())


# index(value, [start], [end]) - выводит занчение value, которое мы передаём, в нашей строке.
# text = "Hello John snow"
# print(text.index("John", 2, 5))

# text = "Hello world! my name is John Snow!"
# print(text.index("Hello"))
# print(text.index("world"))
# print(text.index("John"))
# print(text.index("Snow"))
# res = text.index("o",  + 1)
# print(res) 4
# res = text.index("o", res + 1)
# print(res) 7
# res = text.index("o", res + 1)
# print(res) 
# res = text.index("o", res + 1)
# print(res)

# count(value, [start]) - считает кол-во вхождений value в нашу строку 

# text = "hello o o o hello "
# print(text.count("o"))
# print(text.count("hello"))

# split(separator) - дробит нащу строку по разделителю все части строк сохраняются в типе list


# text = "kalli uchis jastin timberlake hfhfhfhf hfhfhfhfhf"
# res = text.split(" ")
# print(res)
# print(len(res))

# a = "Hello#hello#hello#hello"
# res = a.split("#")
# print(res)

# "conector".join(list) -> соединяет по conector строки 
# которые находилисб в сплит

# text = "kalli uchis jastin timberlake hfhfhfhf hfhfhfhfhf"
# res = text.split(" ")
# print(res)
# str1 = "#".join(res)
# print(str1)

# find(value, [start, [end]]) - делает то же самое что и index, но еслне нашел то вернется -1

# text = "hello"
# print(text.find("l"))
# print(text.find("ascas"), type(text.find("ascas")))

# swapcase() - переводит все символы  в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = "Hello WoRlD, JOHN snow"
# print(f"Oroginal: {text}")
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitalize() - переводит самый первый символ в верхний регистр
# title() - переводит первый символ всех слов в верхний региcтр

# name = input("vvedite imy:").capitalize()
# print(name)
# print(f"Hello! mr/ms {name}" )


# fio = "john edart snow"
# print(fio.title())
# print(dir(str))