from datetime import datetime

# Vraag de geboortedatum van de gebruiker
geboortedatum_str = input("Wat is je geboortedatum? (dd-mm-jjjj): ")
geboortedatum = datetime.strptime(geboortedatum_str, "%d-%m-%Y")
vandaag = datetime.today()

# Bereken de leeftijd
leeftijd = vandaag.year - geboortedatum.year - ((vandaag.month, vandaag.day) < (geboortedatum.month, geboortedatum.day))

# Bepaal wat de gebruiker mag volgens de Nederlandse wet
if leeftijd >= 24:
    print("Je mag alle motoren rijden (A).")
elif leeftijd >= 21:
    print("Je mag zware motoren rijden met code 80 (A met code 80).")
elif leeftijd >= 20:
    print("Je mag middelzware motoren rijden (A2).")
elif leeftijd >= 18:
    print("Je mag lichte motoren rijden (A1).")
else:
    print("Je mag nog niet motorrijden.")
    
# Vraag de geboortedatum van de gebruiker.
# En toon wat deze gebruiker vandaag volgens de Nederlandse wet mag op het gebied van motorrijden.
