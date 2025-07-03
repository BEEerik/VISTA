def is_getal():
    try:
        nr1 = float(input("Voer het 1e getal in: "))
        nr2 = float(input("Voer het 2e getal in: "))
        print(f"Beide ingevoerde waarden zijn getallen: {nr1} en {nr2}")
    except ValueError:
        print("Een of beide ingevoerde waarden zijn geen getallen. Probeer het opnieuw.")

is_getal()

"""
02_is_getal.py
Vraag een gebruiker om twee getallen in te vullen. 
Controleer of de twee getallen ook echt getallen zijn.
"""

