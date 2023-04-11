# Встроеные функции

#  Анонимная функция  - lambda (обычная функция с одной особеностью у нее нет имени)
# Принимат сколько угодно параметров но всегда возвращает одно выражение

# def hello():
#     return "hello" 
# # print(hello())

# x = lambda: "hello"
# print(x())

# x = lambda a, b, c: (a * b) % c
# print(x(5, 5, 5))

# x = lambda num1, num2, degree = 2: (num1 * num2) ** degree if degree else num1 * num2

# print(x(2,2,3))
# print(x(2,2))

# def myFunc(n):
#     return lambda num: num * n
# my_doubler = myFunc(2)
# print(my_doubler(50))

# dict_ = {"john": 500, "tirion": 160_000, "tom": 150,"sanchar": 20 }
# new_dict = dict(sorted(dict_.items(), key = lambda x: x[1], reverse = True))
# print(new_dict)

# map(function, iterable) - применяется к каждому элементу внутри iterable функции
# которкю мы предаем в function закилвая результат те данные которве возврашает функция. В результате мы получаем mapobject(iterable),
# в котором хранятся все наши данные. 

# ls = ["one", "two", "three", "four"]

# new_list  = list(map(lambda x: x.capitalize, ls))
# print(new_list)

# names = ["john", "aria", "baku", "bakberdi"]
# new_list = list(map(lambda x: f"hello, mr/mrs {x}", names))
# print(new_list)

# Фугкция выщего порядка = функция котороя принемает принимает в качестве аргумента другую функцию

# filter(function, iterable) - применяет ко всем элементам itarable функцию котрую мы передали  и возвращает filterobject(итератор) 
# только с теми элементами для которыз  функция вернула True 

# ls = ["one", "lili", "oleg", "billi", "tirion"]
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)

# enumerate(iterable) - пронумеровывает каждый элемент внутри iterable к собственным индексом 

# ls = ["str1", "str2", "str3"]
# new_list = list(enumerate(ls))
# print(new_list)

# zip(iterable) - она соединяет каждый элемент итеррируемых обьектов между собой в тип данных tuple и возврщает итератор


# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]

# res = dict(zip(ls1, ls2))
# print(res)

# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500, 600]
# ls3 = [10, 20, 30]
# res = list(zip(ls1, ls2, ls3))
# print(res)


# zip для создания словарей 
# d_keys = ["hostname", "location", "vendor", "model", "IP"]
# data = {
#     "oktbr": ["bishkek_oktbr", "Gorkaya 212", "Vefa", "Cisco", "10.255.012"],
#     "1may": ["bishkek_1may", "Jibek-jolu 212", "Beliy dom", "Cisco", "11.255.11.12"],
#     "svrdl": ["bishkek_svrdl", " Ahunbaeva 212", "TC", "Cisco", "10.255.105.12"],

# }
# bishkek_data = {}

# for k in data:
#     bishkek_data[k] = dict(zip(d_keys, data[k]))

# print(bishkek_data) 

# ----------------------------------------------------------------------------------------------

# all() , any()

# all(iterable) - Возвращает True если все элементы итерируемые обьекты истина, иначе False
 

# ls = [5, 6, 7, []]
# print(all(ls))


# ip = "10.255.0.155"# True
# ip1 = "10,124.0y.155"# False


# result = all(x.isdigit() for x in ip1.split("."))

# print(result)


# any - Возвращает True, если хотябы один элемент истинна

# ls = [0, 0, [], 0]
# print(any(ls)) 


# ignore = ["rm -rf", "sudo", "reset", "poweroff"]
# command = input("vvedite commandu: ")

# if any(x in command for x in ignore):
#     raise Exception("Block you!")
# print("it\'s okey")

# -------------------------------------------------------


# from random import choices
# from string import ascii_letters, digits 
# from itertools import repeat

# symbols = "_()+-@!#%"
# q_pass = int(input("vvedite kol-vo paroley: "))
# res = {
#     f(choices(ascii_letters, k = 15), choices(digits, k = 6),choices(symbols, k = 2))
#     for f in repeat(lambda x, y, z: "".join(set(x+y+z)), q_pass)
# }
# print(res)
# print(f"Quantity of password: {len(res)}")
# from statistics import mean
# avg = mean(len(x) for x in res)
# print(f"Avg len of passwords: {avg}")



#  Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. 
# Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, 
# который определен в этой функции. 
# То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.

size = 12

def size_second():
    global size
    size_2 = 10
    size_2 = size + size_2
    def size_three():
        nonlocal size_2
        size_3 = 8
        size_3 = size_2 + size_3
        return size_3
    return size_three()

print(size_second())

