# Uitleg: Roulette Simulator in Python

Dit document beschrijft het Python-script `roulette_simulator.py`, een eenvoudige roulette-simulator die perfect is voor studenten om te oefenen met fundamentele programmeerconcepten zoals **loops**, **conditionals** (voorwaardelijke statements) en het gebruik van de **`random` module**.

## Spelregels

De simulator volgt de basisregels van een eenvoudig roulettespel:

* **Startkapitaal**: Je begint met 10 chips.
* **Inzet**: Je kiest hoeveel chips je wilt inzetten per ronde.
* **Getal kiezen**: Je kiest een enkel getal tussen 0 en 36 om op in te zetten.
* **Wiel draaien**: Het programma simuleert een draai aan het roulettewiel en kiest een willekeurig winnend getal (ook tussen 0 en 36).
* **Winst**: Als je gekozen getal overeenkomt met het gedraaide getal, win je **35 keer je inzet**. Zo niet, dan verlies je je inzet.
* **Doorgaan/Stoppen**: Na elke ronde kun je kiezen om door te gaan, zolang je saldo dit toelaat. Het spel eindigt wanneer je kiest om te stoppen of wanneer je saldo 0 chips bereikt.

## Hoe het `roulette_simulator.py` script werkt

Het script is opgebouwd rondom de functie `speel_roulette()`, die de gehele spelcyclus beheert.

1.  **Initialisatie**:
    * `saldo = 10`: De speler begint met 10 chips. Dit is een **variabele** die tijdens het spel verandert.

2.  **Hoofdlus (`while saldo > 0:`)**:
    * Dit is de belangrijkste **loop** (lus) van het spel. Het zorgt ervoor dat het spel doorgaat zolang de speler nog chips heeft (`saldo > 0`).

3.  **Inzet vragen (`while True: ...`)**:
    * Een **geneste `while` loop** wordt gebruikt om herhaaldelijk te vragen naar de inzet van de speler totdat er een geldige invoer is.
    * **`try-except` blok**: Dit is een belangrijk concept voor **foutafhandeling**. Het probeert de invoer om te zetten naar een geheel getal (`int()`). Als de gebruiker bijvoorbeeld tekst invoert in plaats van cijfers (een `ValueError`), wordt dit opgevangen en wordt een foutmelding getoond zonder dat het programma crasht.
    * **Conditionals (`if 0 < inzet <= saldo:`)**: Dit controleert of de inzet een positief getal is en niet meer dan het huidige saldo van de speler.

4.  **Getal kiezen (`while True: ...`)**:
    * Vergelijkbaar met de inzet, wordt hier gevraagd naar het getal waarop de speler wil inzetten. Ook hier wordt **inputvalidatie** en **foutafhandeling** gebruikt om ervoor te zorgen dat het getal tussen 0 en 36 ligt.

5.  **Wiel draaien (`gedraaid_getal = random.randint(0, 36)`)**:
    * De **`random` module** komt hier in actie. `random.randint(0, 36)` genereert een willekeurig geheel getal tussen 0 en 36 (inclusief beide getallen), wat het resultaat van de roulettewiel-draai simuleert.

6.  **Resultaat controleren (`if gekozen_getal == gedraaid_getal: ... else: ...`)**:
    * Dit is een **conditional** (`if/else` statement) die bepaalt of de speler heeft gewonnen of verloren.
    * Als de getallen overeenkomen, wordt de winst berekend (`inzet * 35`) en bij het saldo opgeteld.
    * Als de getallen niet overeenkomen, wordt de inzet van het saldo afgetrokken.

7.  **Doorgaan of stoppen (`if saldo > 0: ... else: ...`)**:
    * Na elke ronde, als het saldo nog steeds positief is, wordt de speler gevraagd of hij wil doorgaan.
    * Opnieuw wordt een **geneste `while` loop** en **inputvalidatie** gebruikt om een "ja" of "nee" antwoord af te dwingen.
    * Als de speler "nee" kiest, wordt de functie beëindigd (`return`), wat het spel stopt.
    * Als het saldo 0 is, wordt een "Game over" bericht getoond en stopt de hoofdlus automatisch.

## Hoe je het script uitvoert

Volg deze stappen om de `roulette_simulator.py` te gebruiken:

1.  **Sla het bestand op**: Kopieer de Python-code hierboven en sla deze op als `roulette_simulator.py` op je computer (bijvoorbeeld in een map genaamd `PythonGames`).
2.  **Open een terminal of commandoregel**:
    * **Windows**: Zoek naar `cmd` in het Startmenu.
    * **macOS**: Open `Terminal` via `Programma's` > `Hulpprogramma's`.
    * **Linux**: Open je favoriete terminal.
3.  **Navigeer naar de map**: Gebruik het `cd` commando om naar de map te gaan waar je `roulette_simulator.py` hebt opgeslagen.
    * Voorbeeld (Windows): `cd C:\Users\JouwNaam\Documents\PythonGames`
    * Voorbeeld (macOS/Linux): `cd ~/Documents/PythonGames`
    (Vervang `JouwNaam` met je daadwerkelijke gebruikersnaam).
4.  **Voer het script uit**: Typ het volgende commando en druk op Enter:
    ```bash
    python roulette_simulator.py
    ```
5.  **Speel het spel**: Volg de instructies op het scherm om je inzet te plaatsen, een getal te kiezen, en te zien of je wint of verliest!