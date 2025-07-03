while True:
    
    getal = float(input("Geef een getallen waarvan u de faculteit wil berekenen: "))    
    if getal < 0:
        print("Faculteit is niet gedefinieerd voor negatieve getallen.")
    elif getal == 0:
        print("De faculteit van 0 is 1.")
    else:
        faculteit = 1
        for i in range(1, int(getal) + 1):
            faculteit *= i
        print(f"De faculteit van {getal} is {faculteit}.")
    again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
    break

    
"""
09 Faculteit
Maak een programma dat de faculteit van een door de gebruiker ingevoerd getal kan 
berekenen en op het scherm toont.

Python
if… else-instructie
for Loop

De faculteit van een getal is het product van alle gehele getallen van 1 tot dat getal.
De faculteit van 6 is bijvoorbeeld 1*2*3*4*5*6 = 720. 
Faculteit is niet gedefinieerd voor negatieve getallen en de faculteit van nul één 0! = 1.
"""