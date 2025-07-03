while True:
    
    getal_1 = float(input("Geef 3 getallen door. Wat is je 1e getal: ? "))
    getal_2 = float(input("Wat is je 2e getal: ? "))
    getal_3 = float(input("Wat is je 3e getal: ? "))

    try:
        resultaat = getal_1 / getal_2 / getal_3
        print(f"Het resultaat is: {resultaat:.4f}")
    except ZeroDivisionError:
        print("Delen door nul is niet toegestaan.")
    
    again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
        break
    
    
"""
08 Delen
Vraag de gebruiker om 3 getallen in te voeren. Het
programma deelt deze 3 getallen door elkaar 
en toont de uitkomst op vier decimalen nauwkeurig op het scherm.
"""

