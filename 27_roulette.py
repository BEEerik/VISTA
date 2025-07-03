import random

def speel_roulette():
    """
    Simuleert een eenvoudig roulettespel.
    De speler begint met 10 chips en kan inzetten op een getal tussen 0 en 36.
    Wint 35x de inzet bij correcte voorspelling.
    """
    saldo = 10
    print("Welkom bij de Roulette Simulator!")
    print(f"Je begint met {saldo} chips.")

    while saldo > 0:
        print(f"\nHuidig saldo: {saldo} chips.")

        # Inzet vragen
        while True:
            try:
                inzet = int(input("Hoeveel chips wil je inzetten? "))
                if 0 < inzet <= saldo:
                    break
                else:
                    print(f"Ongeldige inzet. Je moet tussen 1 en {saldo} chips inzetten.")
            except ValueError:
                print("Ongeldige invoer. Voer een heel getal in voor je inzet.")

        # Getal kiezen
        while True:
            try:
                gekozen_getal = int(input("Op welk getal (0-36) wil je inzetten? "))
                if 0 <= gekozen_getal <= 36:
                    break
                else:
                    print("Ongeldig getal. Kies een getal tussen 0 en 36.")
            except ValueError:
                print("Ongeldige invoer. Voer een heel getal in voor je getal.")

        # Roulettewiel draaien
        gedraaid_getal = random.randint(0, 36)
        print(f"\nHet roulettewiel draait... Het balletje landt op: {gedraaid_getal}!")

        # Resultaat controleren
        if gekozen_getal == gedraaid_getal:
            winst = inzet * 35
            saldo += winst
            print(f"Gefeliciteerd! Je getal {gekozen_getal} kwam overeen!")
            print(f"Je wint {winst} chips. Je saldo is nu {saldo} chips.")
        else:
            saldo -= inzet
            print(f"Helaas, het was {gedraaid_getal}. Je verliest {inzet} chips.")
            print(f"Je saldo is nu {saldo} chips.")

        # Doorgaan of stoppen
        if saldo > 0:
            while True:
                doorgaan_keuze = input("Wil je nog een keer spelen? (ja/nee) ").lower()
                if doorgaan_keuze in ['ja', 'j']:
                    break
                elif doorgaan_keuze in ['nee', 'n']:
                    print("Bedankt voor het spelen! Je eindigt met", saldo, "chips.")
                    return # Beëindig de functie
                else:
                    print("Ongeldige invoer. Antwoord met 'ja' of 'nee'.")
        else:
            print("Je saldo is 0 chips. Helaas, je hebt geen chips meer om te spelen.")
            print("Game over!")

if __name__ == "__main__":
    speel_roulette()