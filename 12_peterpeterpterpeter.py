while True:
    naam = (input("wat is je naam? "))
    print(f"{naam*4}")
    
    aantal  = int(input("Hoe vaak wil je je naam herhalen? "))
    print(f"{naam*aantal}")
    
    again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
        break
    
"""
PeterPeterPeterPeter 2
Vraag de gebruiker om zijn naam voornaam in te vullen 
en het aantal keer dat de naam achterelkaar gezet moet worden.
Zorg dat de naam zoveel keer achterelkaar gezet wordt.
"""	