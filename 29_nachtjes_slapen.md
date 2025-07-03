# Uitleg: Nachtjes Slapen - Datumverschil Calculator

Dit document beschrijft het Python-script `nachtjes_slapen.py`, dat is ontworpen om het aantal dagen tussen een door de gebruiker opgegeven datum en de huidige datum te berekenen. Het is een uitstekende oefening voor het werken met datums en tijden in Python, met name de `datetime.date` klasse.

## Hoe het werkt

Het script gebruikt de `date` klasse uit de ingebouwde `datetime` module van Python. Deze module biedt klassen voor het manipuleren van datums en tijden.

1.  **Huidige Datum Ophalen**:
    * `from datetime import date`: Importeert specifiek de `date` klasse uit de `datetime` module.
    * `vandaag = date.today()`: Deze regel haalt de huidige datum van de computer op.

2.  **Gebruikersinvoer**:
    * Het programma vraagt de gebruiker om het jaar, de maand en de dag in te voeren.
    * **Input Validatie**: Er wordt gebruik gemaakt van een `while True` lus en een `try-except` blok om ervoor te zorgen dat de gebruiker geldige numerieke invoer geeft en dat de combinatie van jaar, maand en dag een *bestaande* datum vormt (bijvoorbeeld, het voorkomt dat je 31 februari invoert). Als de invoer ongeldig is, wordt de gebruiker gevraagd het opnieuw te proberen.

3.  **Datum Object Creëren**:
    * `ingevoerde_datum = date(jaar, maand, dag)`: Zodra geldige getallen zijn ingevoerd, wordt hiermee een `date`-object gemaakt voor de door de gebruiker opgegeven datum.

4.  **Verschil Berekenen**:
    * `verschil = ingevoerde_datum - vandaag`: Python maakt het heel eenvoudig om het verschil tussen twee `date`-objecten te berekenen. Het resultaat is een `timedelta`-object.
    * `aantal_dagen = verschil.days`: Uit het `timedelta`-object halen we het aantal dagen via de `.days` attribuut.

5.  **Resultaat Weergeven**:
    * **Conditionals (`if/elif/else`)**: Het script gebruikt voorwaardelijke statements om te bepalen of de ingevoerde datum in de toekomst, in het verleden, of precies vandaag is.
    * Als `aantal_dagen` positief is, ligt de datum in de toekomst.
    * Als `aantal_dagen` negatief is, lag de datum in het verleden. We gebruiken `{-aantal_dagen}` om het absolute aantal dagen weer te geven (bijv. -12 dagen wordt "12 dagen geleden").
    * Als `aantal_dagen` nul is, is de ingevoerde datum gelijk aan vandaag.

## Hoe je het script uitvoert

Volg deze stappen om het `nachtjes_slapen.py` script te gebruiken:

1.  **Maak een map aan**: Maak een nieuwe map op je computer (bijv. `DatumCalculator`).
2.  **Maak `nachtjes_slapen.py`**:
    * Open een teksteditor (Kladblok, Visual Studio Code, etc.).
    * Kopieer de volledige Python-code van "Bestand 1: `nachtjes_slapen.py`" hierboven.
    * Plak het in de teksteditor en sla het op als `nachtjes_slapen.py` in de zojuist aangemaakte map. Zorg ervoor dat de extensie `.py` is.
3.  **Maak `nachtjes_slapen_uitleg.md`**:
    * Open een **nieuw** leeg bestand in je teksteditor.
    * Kopieer de volledige Markdown-tekst van dit document (`nachtjes_slapen_uitleg.md`).
    * Plak het in de teksteditor en sla het op als `nachtjes_slapen_uitleg.md` in **dezelfde map**. Zorg ervoor dat de extensie `.md` is.
4.  **Voer het Python-script uit**:
    * Open je terminal of commandoregel (CMD op Windows, Terminal op macOS/Linux).
    * Navigeer naar de map waar je de bestanden hebt opgeslagen met het `cd` commando (bijv. `cd C:\Gebruikers\JouwNaam\DatumCalculator`).
    * Typ `python nachtjes_slapen.py` en druk op Enter.
5.  **Volg de instructies**: Het programma zal je vragen om het jaar, de maand en de dag in te voeren.

## Voorbeelden van de output

De output zal variëren afhankelijk van de huidige datum en de datum die je invoert.
