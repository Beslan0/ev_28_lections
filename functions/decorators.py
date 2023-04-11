# Декораторы - это функция которая позволяет без изменения кода функции расширить его функционал 


# def decorator(func):
#     print(func)
#     func()
# def hello():
#     print("Hello stranger!")

# def john():
#     print("My nsme is John Snow! i\'m King of North!")
# # hello()
# # print(hello)

# decorator(hello)
# print("!!!!!")
# decorator(john)

# pyhtonic way -> @
# синтаксические сахар - красота кода

# def decorator(func):
#     def wrapper():
#         print(f"мы вызвали функцию: {func.__name__}")
#         func()
#     return wrapper    

# @decorator
# def john():
#      print("My nsme is John Snow! i\'m King of North!")

# @decorator
# def hello():
#      print("Hello stranger")

# hello()
# print()
# john()



# def benchnark(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time() 
#         func(*args,**kwargs)
#         finish = time.time()
#         print(f"время выполнения функции {func.__name__}, заняло: {finish - start}")
#     return wrapper

# @benchnark
# def loop():
#     i = 0
#     range_number = 100_000_000
#     while i < range_number:
#         # print(i) 
#         i += 1
        



# @benchnark
# def add(number):
#     i = 0
#     # range_number = 100_000_000
#     ls = []
#     while i < number:
        
#         ls.append(i)
#         i += 1
#         # print(ls)

# loop()
# add(100_000_000)


# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = "<bold>" + func(*args, **kwargs) + "</bold>"
#         return res 
#     return wrapper


# def div(func):
#      def wrapper(*args, **kwargs):
#         res = "<div>" + func(*args, **kwargs) + "</div>"
#         return res 
#      return wrapper

# @bold
# @div
# @bold 
# def str_(name):
#     return name


# print(str_("John Snow"))

    # ------------------------------------------------------------
# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f"Trace: вызвала {func.__name__}() \nона приняла args: {args}, kwargs: {kwargs}")
        
#         original_result = func(*args,**kwargs)
        
#         print(f"Trace: вызвала {func.__name__}() \nона вернула: {original_result} ")
#         return original_result
#     return wrapper


# @trace
# def say(name,address):
#     return f"{name} --> {address}"
# @trace
# def hello(name, last_name, country):
#     return f"Hello {name} {last_name} from {country}!"

# say("Sherlock Hplms", "Bakery street 221B")
# print()
# hello("Homer","Simpson", "Canada")

# name_of_list = ['Helloworld!']
# amount = len(name_of_list)
# print(amount)
# if len(name_of_list) % 2 == 0:
#     first_half = list(name_of_list[:amount])
#     second_half = list(name_of_list[amount:])
# else:
#     second_half = list(name_of_list[:amount+1])
#     first_half = list(name_of_list[amount:+1])
# new_list = []
# for char in second_half + first_half:
#     list(new_list.append(char))

# print(new_list)

# def decorator(func):
#     def wrapper():
#         print(f"This finction named {func.__name__}")
#         func()
#         return wrapper

# @ decorator
# def hello():
#     print("Hello")

def sq(func):
    def wrapper(num):
        nums = func(num)
        return list(map(lambda x: x **2, nums))
    return wrapper
@sq
def func(num: int):
    return list(range(1, num))



print(func(5))
