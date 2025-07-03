def bereken_totaal_punten():
    """
    Berekent het totale aantal punten op basis van gewogen categorieën.
    """
    print("Welkom bij de Gewogen Cijfercalculator!")
    print("---------------------------------------")
    print("Voer het aantal correcte antwoorden in per categorie.")

    # Definieer de weging per categorie
    # Categorie_nummer: Punten_per_stuk
    wegingen = {
        1: 10,
        2: 20,
        3: 40,
        4: 80
    }

    totaal_punten = 0

    # Loop door elke categorie en vraag om invoer
    for categorie_nummer, punten_per_stuk in wegingen.items():
        while True:
            try:
                aantal_goed_str = input(f"Hoeveel van categorie {categorie_nummer} is goed? (Elk telt voor {punten_per_stuk} punten): ")
                aantal_goed = int(aantal_goed_str)
                if aantal_goed >= 0: # Aantal kan 0 of positief zijn
                    break
                else:
                    print("Het aantal kan niet negatief zijn. Voer een positief getal of 0 in.")
            except ValueError:
                print("Ongeldige invoer. Voer een heel getal in.")
        
        # Bereken de punten voor deze categorie en tel op bij het totaal
        punten_categorie = aantal_goed * punten_per_stuk
        totaal_punten += punten_categorie
        print(f"  > Punten voor categorie {categorie_nummer}: {punten_categorie}")

    print("\n---------------------------------------")
    print(f"Het **totaal aantal behaalde punten** is: {totaal_punten}")
    print("Bedankt voor het gebruiken van de calculator!")

if __name__ == "__main__":
    bereken_totaal_punten()