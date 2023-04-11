import random

number = random.randint(1, 5)
attempt = 1
name = input("what is your name? ")
star = input(f"{name}  start game? ")

for i in range(3):
    
    if star == "No".lower():
        print(f"bye bye {name}")
        break 
    
    elif  star == "Yes".lower():
        a = input("gues the number: ")
        a ==  number
        print(f"Nise {name} you guessed number {attempt} attempt")
        break
    
    elif i != 2: 
        print("sorry but you dont guessed!")
        attempt += 1
        restart = input(f"try again! {name} ")
        a = input("gues the number: ")
        a == number
        print(f"Nise {name} you guessed number {attempt} attempt")
        break



    