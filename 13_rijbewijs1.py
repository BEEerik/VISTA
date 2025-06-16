# Vraag de leeftijd van de gebruiker
while True:
    leeftijd = int(input("Wat is je leeftijd? "))

    # Controleer of de gebruiker mag autorijden
    if leeftijd >= 18 and leeftijd <= 80:
        print("Je mag autorijden.")
    elif leeftijd > 80:
        print("Je mag geen auto meer rijden.")
    else:
        print("Je mag nog niet autorijden.")
    
    again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
        break