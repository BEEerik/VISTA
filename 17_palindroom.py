def is_palindroom(woord):
    """
    Controleert of een gegeven woord een palindroom is.
    Een palindroom leest hetzelfde van voor naar achteren als van achteren naar voren.
    Hoofdletters en spaties worden genegeerd.
    """
    # Verwijder spaties en maak alles lowercase voor een consistente vergelijking
    schoongemaakt_woord = "".join(filter(str.isalnum, woord)).lower()
    
    # Keer het schoongemaakte woord om
    omgekeerd_woord = schoongemaakt_woord[::-1]
    
    # Vergelijk het schoongemaakte woord met het omgekeerde woord
    return schoongemaakt_woord == omgekeerd_woord

if __name__ == "__main__":
    print("Welkom bij de Palindroom Checker!")
    print("--------------------------------")
    
    while True:
        invoer_woord = input("Voer een woord of zin in (typ 'stop' om te eindigen): ")
        
        if invoer_woord.lower() == 'stop':
            print("Bedankt voor het gebruik van de Palindroom Checker. Tot ziens!")
            break
        
        if is_palindroom(invoer_woord):
            print(f"'{invoer_woord}' is een palindroom!")
        else:
            print(f"'{invoer_woord}' is geen palindroom.")
        print("-" * 30)