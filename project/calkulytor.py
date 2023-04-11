num1 = float(input("vvedite chislo: "))
oper = input("vvedite operaciy: ")
num2 = float(input("vvedite chislo: "))
otvet = ("Otvet: ")

if oper == "+":
    print(f"{otvet} {num1 + num2}")

elif oper == "-":
    print(f"{otvet} {num1 - num2}")

elif oper == "*":
    print(f"{otvet} {num1 * num2}")

elif oper == "**":
    print(f"{otvet} {num1 ** num2}")

elif oper == "/":
    print(f"{otvet} {num1 / num2}")

elif oper == "//":
    print(f"{otvet} {num1 // num2}")

elif oper == "%":
    print(f"{otvet} {num1 % num2}")

else:
    print("Ne vernaiy operaciy")