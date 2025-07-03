from datetime import date

def bereken_datumverschil():
    """
    Vraagt de gebruiker om een datum (jaar, maand, dag) en berekent
    het verschil in dagen met de huidige datum.
    """
    print("Welkom bij de Datumverschil Calculator!")
    print("------------------------------------")

    while True:
        try:
            jaar = int(input("Voer het jaar in (bijv. 2023): "))
            if not (1 <= jaar <= 9999): # Eenvoudige validatie voor jaar
                print("Ongeldig jaar. Voer een jaar tussen 1 en 9999 in.")
                continue

            maand = int(input("Voer de maand in (1-12): "))
            if not (1 <= maand <= 12):
                print("Ongeldige maand. Voer een getal tussen 1 en 12 in.")
                continue

            dag = int(input("Voer de dag in (1-31): "))
            if not (1 <= dag <= 31): # Eenvoudige validatie voor dag
                print("Ongeldige dag. Voer een getal tussen 1 en 31 in.")
                continue

            # Probeer de datum te maken om te controleren op geldigheid (bijv. 31 februari)
            ingevoerde_datum = date(jaar, maand, dag)
            break # Als de datum geldig is, stop de lus
        except ValueError:
            print("Ongeldige invoer. Zorg ervoor dat je geldige getallen invoert voor jaar, maand en dag.")
        except Exception as e:
            print(f"Er is een fout opgetreden bij het maken van de datum: {e}. Probeer opnieuw.")

    vandaag = date.today() # Haalt de huidige datum op

    verschil = ingevoerde_datum - vandaag
    aantal_dagen = verschil.days

    print(f"\nDe ingevoerde datum is: {ingevoerde_datum}")
    print(f"Vandaag is: {vandaag}")

    if aantal_dagen > 0:
        print(f"De ingevoerde datum ligt {aantal_dagen} dagen in de toekomst.")
    elif aantal_dagen < 0:
        print(f"De ingevoerde datum lag {-aantal_dagen} dagen geleden.")
    else:
        print("De ingevoerde datum is vandaag!")

    print("\nBedankt voor het gebruiken van de Datumverschil Calculator!")

if __name__ == "__main__":
    bereken_datumverschil()