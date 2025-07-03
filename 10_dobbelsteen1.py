# Dobbelsteen nr 1
# Vraag de gebruiker hoeveel dobbelstenen deze wil gooien. 
# Laat zien dat de dobbelstenen gegooid worden, 
# wat het resultaat per dobbelsteen is en 
# wat de som is van het aantal ogen.
# Martin > Erik
import random

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

while True:
    print("Mini Challenge 10: Vraag hoeveel dobbelstenen je wilt gooien, gooi ze en toon de resultaten en de totale som")
    inputDice = input("Hoeveel dobbelstenen wil je gooien? (maximaal 6) ")
    
    if not is_number(inputDice):
        print(f"{inputDice} is geen getal")
        continue
    
    inputDice = float(inputDice)
    
    if inputDice <= 0:
        print("Het aantal moet een positief getal groter dan nul zijn")
        continue
    
    if inputDice > 6:
        print("Het aantal dobbelstenen mag niet meer dan 6 zijn")
        continue
    
    if not is_integer(inputDice):
        inputINT = int(inputDice)
        print(f"Aangezien we geen deel van een dobbelsteen kunnen gooien, ronden we {inputDice} af naar {inputINT}")
    else:
        inputINT = int(inputDice)
    
    TOT = 0
    for i in range(1, inputINT + 1):
        D = random.randint(1, 6)
        TOT += D
        print(f"Rol dobbelsteen {i}: {D}")
    
    print(f"De totale som van alle dobbelstenen is: {TOT}")
    
    again = input("Nog een keer gooien? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
        break

