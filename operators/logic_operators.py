# операторы сравнения 
# условные рпреаторы и логические операторы

# операторы сравнения

# <, >, ==(равно), !=(не равно), <=, >=

# 1 < 5 -> True
# 7 > 9 -> False

# условные операторы 

# if
# elif
# else

# if <condition>:
#     <body if> # сработает если вы в condition if придет True

# [elif] <condition>
#     <body elif>
# [else]:
#     <body else> # сработает если вы во всех выще стоящих условия пришло False 

# string = input("enter smt:")

# if string.lower() == "hello":
#     print("Hello it\'me \n I was wondering if after all these years you\'d like to meet")
# elif string.lower() == "john":
#     print("welcome back john! The king of northe")
# elif string.lower() == "abada-kadabra":
#     print("qwerty")
# else:
#     print("совпадении не найдено")    

# print("Registration form")
# email = input("enter you email")
# pasword =  input("enter you pasword") 

# if len(pasword) < 8:
#     raise ValueError("password is too short~\n need to be 8 symbols or me")14
# elif pasword.isdigit():
#     raise ValueError( "paaswors  is invailed\n password must contain number or special symbols too!")
# elif pasword.isalpha():
#         raise ValueError( "paaswors  is invailed\n password must contain number or special symbols too!")


# pasword2 = input("Enter password confirmation:")

# if pasword != pasword2:
#      raise ValueError("password didnt match")

# print(f"successfully registered! Hello MR/mrs {email}!")

# age = input("enter your age")

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception("invalid value for age ")

# if age < 18:
#     print(f' access denied! come again after {18 - age} year!')
# else:
#     print("you can pass! welcome to KZ")

# and - логичеснкое И
# or  -  лог или
# not -  лог отрицания.

# money = 1_000_000

# status = "premium"

# if money < 1_000_000 and status == "premium":
#     print("you are president of our club!")

# elif money > 1_000_000 or status == "premium":
#     print("you are ministr of our club!")

# else:
#     print("you are honorable member of our club!")
# str1 = "Hello world"
# print(str1)
# symbol = input("enter the synbol: ")

# if symbol not in str1:
#     print(f"The symbol: {symbol} does not exisits!")
# else:
#     print(f"The symbol: {symbol} exists")

# if symbol  in str1:
#     print(f"The symbol: {symbol} does not exists!")
# else:
#     print(f"The symbol: {symbol} exists")


# разрешаем доступ еслт он юзер гита гугла и его возраст больще 21 или у него денег (10000)

# user = "John"
# is_google_user = True
# is_github_user  = False

# age = 19
# user_coins = 9000

# if (is_github_user or is_google_user) and (age > 21 or user_coins > 10000):
#     print(f"you can enter the system Mr/Mrs {user}!")
# else:
#     print("you can not enter the system") 