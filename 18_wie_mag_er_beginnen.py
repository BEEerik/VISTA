import random

aantal_spelers = int(input("Hoeveel spelers zijn er? "))

spelers = []
for i in range(aantal_spelers):
    naam = input(f"Wat is de naam van speler {i+1}? ")
    spelers.append(naam)

beginner = random.choice(spelers)
print(f"{beginner} mag beginnen!")

"""
18 Wie mag er beginnen?
Vraag hoeveel spelers er zijn. Vraag vervolgens per speler de naam. Laat op het scherm de naam van een willekeurige speler zien. Deze speler mag beginnen.

Vraag het aantal spelers
Vraag de naam van elke speler
Kies een willekeurige speler om te beginnen
"""