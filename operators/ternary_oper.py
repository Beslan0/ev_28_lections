# sentence = input("Vvedite predlojeniy: ")

# # if sentence [-1] == "?":
# #     print("yes, vopsotel\"noye!")
# # else:
# #     print("no normal one")


# print("yes, vopsotel\"noye!" if sentence[-1] == "?" else "no, normal one !")

# ternary operators(тернарный оператор) - это конструкция которая по своему анолонично констркции if/else,
#  но прри этом записывается в одну строчку

# number = int(input("vvedite chislo: "))

# res = "even number" if number % 2 == 0  else "odd number"
#         # чентное                           # нечентное

# print(res)


# <выражение если True> if <условие> else <выражение если False>

# ls = [55,65,75,89,100,15,6]  

# print(ls)

# choise = input("vvedite max/min: ")

# res = max(ls) if choise.lower().strip() == "max" else min (ls)
# print(res)

# if choise.lower().strip() == "max":
#     print(max(ls))
# elif choise.lower().strip() == "min":
#     print(min(ls))
# else:
#     print("invalid choise")

# res = max(ls) if choise.lower().strip() == "max" else min (ls) if choise.lower().strip() == "min" else "invalid choise"
# print(res)

# flag = True

# symbols = "0123456789-, ."
# while flag:
#     print()
#     num1 = input("vvedite first num: ")
#     is_correct_number = True
#     for x in num1:
#         if x not in symbols:
#             print("вы вели не правильное число!")
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue
    

    

#     num2 = input("vvedite second num: ")
#     for x in num2:
#         if x not in  symbols:
#             print("вы вели не правильное число!")
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue


#     num1 = float(num1) if "." in num1 else int(num1)
#     num2 = float(num2) if "." in num2 else int(num2)

#     # print(num1, type(num1))   
#     # print(num2, type(num1)) 

#     operator = input("ведите оператор(+,-,*,/)").strip()

#     if operator == "+":
#         print(f"результат: {num1 + num2}")
#     elif operator == "-":
#         print(f"результат: {num1 - num2}")
#     elif operator == "*":
#         print(f"результат: {num1 * num2}")
#     elif operator == "/":
#         if num2 == 0:
#             print("на ноль делть нельзя ")
#         else:
#             print(f"результат: {num1 / num2}")
#     else:
#         print("вы вели не правильный оператор")
    
#     choise = input("хотите продолжить (yes/no)?")
#     if choise.lower().strip() != "yes":
#         flag = False
#         print("пока пока!")



    
