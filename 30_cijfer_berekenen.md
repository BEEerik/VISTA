# Uitleg: Gewogen Cijferberekening in Python

Dit document beschrijft het Python-script `gewogen_cijferberekening.py`, dat is ontworpen om een totaal aantal punten te berekenen op basis van verschillende categorieën, waarbij elke categorie een eigen "weging" of puntwaarde per item heeft. Dit programma is een goede manier om te oefenen met **gebruikersinvoer verwerken**, **numerieke berekeningen** uitvoeren, en **itereren** over data (loops).

## Hoe het werkt

Het script volgt de volgende logica:

1.  **Definieer Wegingen**:
    * De verschillende categorieën en hun bijbehorende puntwaarden per "goed" antwoord zijn opgeslagen in een **Python dictionary** genaamd `wegingen`.
    * Bijvoorbeeld: `1: 10` betekent dat elk item in categorie 1 goed is voor 10 punten.

    ```python
    wegingen = {
        1: 10, # Categorie 1: 10 punten per item
        2: 20, # Categorie 2: 20 punten per item
        3: 40, # Categorie 3: 40 punten per item
        4: 80  # Categorie 4: 80 punten per item
    }
    ```

2.  **Initialiseer Totaal Punten**:
    * Er wordt een variabele `totaal_punten` aangemaakt en geïnitialiseerd op `0`. Dit is waar alle berekende punten van elke categorie bij elkaar worden opgeteld.

3.  **Loop door Categorieën**:
    * Een **`for` loop** itereert over elk `categorie_nummer` en de bijbehorende `punten_per_stuk` in de `wegingen` dictionary. Dit betekent dat het programma automatisch de vragen stelt voor elke gedefinieerde categorie.
    * **Gebruikersinvoer**: Binnen de loop wordt de gebruiker gevraagd hoeveel items van de huidige categorie "goed" zijn.
    * **Input Validatie (`try-except` en `while True`)**:
        * Een **`try-except` blok** vangt mogelijke `ValueError` op als de gebruiker iets invoert dat geen geldig getal is (bijv. tekst).
        * Een **`while True` lus** zorgt ervoor dat de vraag wordt herhaald totdat de gebruiker een geldig, niet-negatief heel getal invoert.
    * **Berekening per Categorie**: Het ingevoerde aantal correcte antwoorden wordt vermenigvuldigd met de `punten_per_stuk` voor die categorie. Dit resultaat wordt vervolgens opgeteld bij `totaal_punten`.

4.  **Totaal Resultaat**:
    * Na het doorlopen van alle categorieën, print het programma het **eindresultaat**: het totale aantal behaalde punten.

## Hoe je het script uitvoert

Volg deze stappen om het `gewogen_cijferberekening.py` script te gebruiken:

1.  **Maak een map aan**: Maak een nieuwe map op je computer (bijv. `Cijferberekening`).
2.  **Maak `gewogen_cijferberekening.py`**:
    * Open een teksteditor (Kladblok, Visual Studio Code, etc.).
    * Kopieer de volledige Python-code van "Bestand 1: `gewogen_cijferberekening.py`" hierboven.
    * Plak het in de teksteditor en sla het op als `gewogen_cijferberekening.py` in de zojuist aangemaakte map. Zorg ervoor dat de extensie `.py` is.
3.  **Maak `gewogen_cijferberekening_uitleg.md`**:
    * Open een **nieuw** leeg bestand in je teksteditor.
    * Kopieer de volledige Markdown-tekst van dit document (`gewogen_cijferberekening_uitleg.md`).
    * Plak het in de teksteditor en sla het op als `gewogen_cijferberekening_uitleg.md` in **dezelfde map**. Zorg ervoor dat de extensie `.md` is.
4.  **Voer het Python-script uit**:
    * Open je **terminal** of **commandoregel** (CMD op Windows, Terminal op macOS/Linux).
    * Navigeer naar de map waar je de bestanden hebt opgeslagen met het `cd` commando.
        * Voorbeeld (Windows): `cd C:\Gebruikers\JouwNaam\Cijferberekening`
        * Voorbeeld (macOS/Linux): `cd ~/Documents/Cijferberekening`
        (Vervang `JouwNaam` met je daadwerkelijke gebruikersnaam.)
    * Typ `python gewogen_cijferberekening.py` en druk op Enter.
5.  **Volg de instructies**: Het programma zal je vragen stellen over het aantal correcte antwoorden per categorie.
