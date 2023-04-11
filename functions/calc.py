# def  add(num1: int, num2: int) -> int:
#     return num1 + num2


# def subtract(num1: int or float, num2: int or float) -> int or float:
#     return num1 - num2 

# def multiplay(num1: int or float, num2: int or float) -> int or float:
#     return num1 * num2

# def divide(num1: int or float, num2: int or float) -> int or float:
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         return "На ноль не делится"  

# def calculate(num1: int or float, num2: int or float):
    
#     operator = input("vvedite operator(+,-,*,/) ")
#     if operator == "+": return add(num1,num2)
#     elif operator == "-": return subtract(num1 ,num2)
#     elif operator == "*": return multiplay(num1 ,num2)
#     elif operator == "/": return divide(num1 ,num2)
#     else: return "Вы вели неверный оператор!"

# def main():
#     num1 = input("vvedite chislo: ")
#     num2 = input("vvedite chislo: ")
#     try:
#         num1 = float(num1) if "." in num1 else int(num1)
#         num2 = float(num2) if "." in num2 else int(num2)
#     except ValueError:
#         print("Вы вели некоректоное число!")
#         main()
#         return
    
#     while True:
#         result = calculate(num1, num2)
#         if type(result) == str:
#             print(f"Результат: {result}")
#         else:
#             print(f"Результат: {result}")
#             break
#     question = input("Хотите продолжить?(Yes/No)").lower().strip()
#     if question == "yes":
#         main()

#     else:
#         print("спасибо за исрользование нашего калькулятора ")

# main()