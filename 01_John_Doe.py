"""
def main():
    naam = input("Wat is je naam?")
    print(f"Hello, {naam}")

while True:
    main()
    run_again = input("Wil je nog een keer? (ja/nee)")

    if run_again.lower() == "ja":
        continue
    elif run_again.lower() == "nee":
        break
    else:
        print("Ongeldige invoer. Probeer opnieuw.")
"""
"""
https://www.mbogodigital.nl/python/

01 Hello, John Doe

Vraag de gebruiker om zijn naam in te voeren. 
Als je het script runt dan zie je de tekst "Hello, John Doe" staan. 
John Doe is de ingevoerde naam.

De variabele naam wordt toegewezen aan de invoer van de gebruiker via de input functie. 
De prompt die de gebruiker ziet is "Wat is je naam?".
De print functie wordt gebruikt om een begroeting weer te geven. 
De ingevoerde naam wordt ingevoegd in de string "Hello, {naam}" met behulp van een f-string.
"""

naam = input("Wat is je naam?")
print(f"Hello, {naam}");