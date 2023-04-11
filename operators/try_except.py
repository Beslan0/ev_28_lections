# Обработка исключениий 
# опператроры try...except

# Errors -> связаны с кодом 

# SyntaxError
# IndentationError
# TabError

# Исключения exceptions - связнаы я неправилными данными которые передаются в код

    # ZeroDivisionError
    # ArithmeticError
    # NameError
    # IndexError
    # KeyError
    # BaseException # прородитель всех исключениий 


# try:
#     a = int(input("enter the number: "))
# except:
#     print("неправильные ланные ")
# else:
#     print(a * 5)


# <try>:
#     <body>
# <except>:
#     <body> если есть ошибки
# <else>:
#     <body> если нет ошибки
# <finally>:
#     <body> сработает в любом случае

# ls = ["John", "snow", "tirion"]
# try:
#     i = int(input("vvedite Index: "))
#     print(ls[i])
# except ValueError: 
#     print("вы вели неправильные данные")
# except IndexError:
#     print("вы венли непральные индекс")

# --------------------------------------------------

# отобрпжение ошибки
# Exception as e (error)


# dict_ = {"1": "one", "2": "two", "name": "john"}

# try:
#     key = input("vvedite key: ")
#     print(dict_[key])
# except Exception as e:
#     print(f"Opps Error {e.__class__} error")


# try:
#     num1 = int(input("enter num1: "))
#     num2 = int(input("enter num2: "))
#     result = num1 / num2
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Na 0 delit\' nel\'zya!")
# else:
#     print(result)
# finally:
#     print("The end")



user = input()
if user == user.isdigit:
    print("is digit")
elif user == user.isalpha():
    print("isalpha")


