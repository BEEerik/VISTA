while True:
    
    woord = input("Geef een woord: ")
    
    print (woord[::-1])
    
    again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
        break

"""	
07 Woorden draaien
Vraag om een woord en zorg ervoor dat het omgedraaid op het scherm getoond wordt.

Slicing
minus 1

er is geen start/ stop
-1 geeft aan dat je van achter naar voren wilt gaan
"""	