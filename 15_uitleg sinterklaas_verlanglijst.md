## 15 Sinterklaas verlanglijst

# OPDRACHT
Vraag de gebruiker om in te voeren wat deze graag van Sinterklaas zou willen hebben. 
Vraag één item per keer en blijf vragen tot de gebruiker "KLAAR!" ingetypt heeft.
Toon vervolgens de lijst in alfabetische volgorde op het scherm.

### Sinterklaas Verlanglijst

Dit script vraagt de gebruiker om items voor een verlanglijst in te voeren en toont deze lijst vervolgens in alfabetische volgorde. Het script biedt ook de mogelijkheid om de lijst opnieuw in te voeren.

**Uitleg:**

1. `verlanglijst = []`: Initialiseert een lege lijst om de verlanglijstitems op te slaan.

2. `while True:`: Start een oneindige lus die blijft vragen om invoer totdat de gebruiker "KLAAR!" typt.

3. `item = input("Wat zou je graag van Sinterklaas willen hebben? (typ 'KLAAR!' om te stoppen): ")`: Vraagt de gebruiker om een item in te voeren.

4. `if item.upper() == "KLAAR!":`: Controleert of de gebruiker "KLAAR!" heeft getypt (ongeacht hoofdletters of kleine letters).

5. `break`: Stopt de lus als de gebruiker "KLAAR!" heeft getypt.

6. `verlanglijst.append(item)`: Voegt het ingevoerde item toe aan de verlanglijst.

7. `verlanglijst.sort()`: Sorteert de verlanglijst in alfabetische volgorde.

8. `print("Je verlanglijst in alfabetische volgorde:")`: Print een bericht dat aangeeft dat de verlanglijst in alfabetische volgorde wordt weergegeven.

9. `for item in verlanglijst:`: Itereert door elk item in de gesorteerde verlanglijst.

10. `print(item)`: Print elk item in de verlanglijst.

11. `while True:`: Start een nieuwe oneindige lus om te vragen of de gebruiker opnieuw wil proberen.

12. `again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()`: Vraagt de gebruiker of ze nog een keer willen proberen en zet de invoer om naar kleine letters.

13. `if again in ['nee', 'n']:`: Controleert of de gebruiker "nee" of "n" heeft getypt.

14. `print("Tot ziens!")`: Print een afscheidsgroet.

15. `break`: Stopt de lus als de gebruiker "nee" of "n" heeft getypt.

16. `elif again in ['ja', 'j']:`: Controleert of de gebruiker "ja" of "j" heeft getypt.

17. `verlanglijst = []`: Initialiseert een nieuwe lege verlanglijst.

18. Herhaalt de stappen 2 t/m 10 om een nieuwe verlanglijst in te voeren en te sorteren.

19. `else:`: Als de invoer ongeldig is, print een foutmelding en vraagt opnieuw.
