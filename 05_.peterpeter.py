while True:
    naam = (input("wat is je naam? "))
    print(f"{naam*4}")
    
    again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
        break


"""
05 PeterPeterPeterPeter
Vraag de gebruiker om zijn naam voornaam in te vullen. 
Zorg dat de naam vier keer achterelkaar gezet wordt.
"""	
