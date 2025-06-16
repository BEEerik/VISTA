def is_getal(waarde):
    try:
        float(waarde)
        return True
    except ValueError:
        return False

while True:
    getal1 = input("wat is je 1e getal: ")
    getal2 = input("wat is je 2e getal: ")

    if is_getal(getal1) and is_getal(getal2):
        print("Alle twee nrs zijn een getal")
    else:
        print("een of twee nrs zijn geen getal")
    
    again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
        break

""""
https://www.mbogodigital.nl/python
11.Is Getal?
Vraag een gebruiker om twee getallen in te vullen. 
Controleer of de twee getallen ook echt getallen zijn.
gebruikte functie [is_getal]
"""