# 16 Vermenigvuldigen
# Vraag de gebruiker om 2 getallen in te voeren.
# Gebruik een functie om het product uit te rekenen. 
# Toon het resultaat van de functie op het scherm.
# De functie zelf mag dus niets op het scherm plaatsen.

def vermenigvuldig(getal1, getal2):
    return getal1 * getal2

getal1 = int(input("Geef een getal: "))
getal2 = int(input("Geef nog een getal: "))

resultaat = vermenigvuldig(getal1, getal2)
print(f"Het product van {getal1} en {getal2} is {resultaat}.")