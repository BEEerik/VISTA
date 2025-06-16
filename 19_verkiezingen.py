from collections import Counter

stemmen = []

while True:
    naam = input("Voer een naam in (of 'UITSLAG!' om te stoppen): ")
    if naam.upper() == "UITSLAG!":
        break
    stemmen.append(naam.strip().lower())

if stemmen:
    telling = Counter(stemmen)
    winnaar, aantal = telling.most_common(1)[0]
    print(f"De winnaar is: {winnaar.capitalize()} met {aantal} stemmen.")
else:
    print("Er zijn geen stemmen uitgebracht.")
    
    
#19.Verkiezingen
# Gebruikers mogen net zo lang namen invoeren tot er "UITSLAG!" ingevoerd wordt. De naam die het vaakst ingevoerd is wordt op het scherm getoond als de winnaar. Bij het invoeren maken hoofdletters geen verschil.


