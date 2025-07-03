import random

def gooi_dobbelstenen(invoer_string):
    """
    Simuleert het gooien van dobbelstenen op basis van de 'AdX' notatie.
    A: aantal dobbelstenen
    X: aantal zijden per dobbelsteen
    Bijvoorbeeld: '2d6' betekent 2 dobbelstenen met 6 zijden.
    """
    invoer_string = invoer_string.lower().strip() # Maak lowercase en verwijder spaties

    if 'd' not in invoer_string:
        return "Fout: Ongeldig formaat. Gebruik de 'AdX' notatie (bijv. '2d6').", False

    delen = invoer_string.split('d')

    if len(delen) != 2:
        return "Fout: Ongeldig formaat. Gebruik de 'AdX' notatie (bijv. '2d6').", False

    try:
        aantal = int(delen[0])
        zijden = int(delen[1])
    except ValueError:
        return "Fout: Aantal dobbelstenen en zijden moeten getallen zijn.", False

    if aantal <= 0 or zijden <= 1:
        return "Fout: Aantal dobbelstenen moet positief zijn en zijden moeten minstens 2 zijn.", False

    resultaten = []
    for _ in range(aantal):
        resultaten.append(random.randint(1, zijden))

    return sum(resultaten), True

if __name__ == "__main__":
    print("Welkom bij de Dobbelsteen Simulator!")
    print("-----------------------------------")
    print("Voer het type dobbelstenen in volgens de 'AdX' notatie (bijv. '2d6' voor twee 6-zijdige dobbelstenen).")
    print("Typ 'stop' om te eindigen.")
    
    while True:
        invoer = input("Welke dobbelstenen wil je gooien? ")
        
        if invoer.lower() == 'stop':
            print("Bedankt voor het gebruiken van de Dobbelsteen Simulator. Tot ziens!")
            break
        
        som, succes = gooi_dobbelstenen(invoer)
        
        if succes:
            print(f"De som van de worpen is: {som}")
        else:
            print(som) # Hier wordt de foutmelding geprint
        print("-" * 30)