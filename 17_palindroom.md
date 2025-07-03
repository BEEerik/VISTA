# Uitleg: Palindroom Checker

Dit document beschrijft het Python-script `palindroom_checker.py`, dat is ontworpen om te controleren of een woord of zin een **palindroom** is. Een palindroom is een woord, zin of reeks die hetzelfde leest van voor naar achteren als van achteren naar voren. Denk aan woorden als "lepel" of zinnen als "Madam, I'm Adam".

## Hoe het werkt

Het Python-script bevat één belangrijke functie: `is_palindroom(woord)`.

1.  **Opschonen van de invoer**: De functie begint met het opschonen van de ingevoerde tekst. Dit betekent:
    * Alle **spaties en leestekens worden verwijderd**.
    * Alle letters worden **omgezet naar kleine letters** (lowercase). Dit zorgt ervoor dat "Racecar" en "racecar" beide als palindroom worden herkend.
    * Voorbeelden: "Racecar" wordt "racecar", "Madam, I'm Adam" wordt "madamimadam".

2.  **Omkeren van de tekst**: Na het opschonen wordt de tekst omgekeerd.
    * Als de opgeschoonde tekst "lepel" is, wordt de omgekeerde tekst ook "lepel".
    * Als de opgeschoonde tekst "auto" is, wordt de omgekeerde tekst "otua".

3.  **Vergelijking**: Ten slotte vergelijkt de functie de **opgeschoonde tekst** met de **omgekeerde tekst**.
    * Als ze **identiek** zijn, is het een palindroom en retourneert de functie `True`.
    * Als ze **niet identiek** zijn, is het geen palindroom en retourneert de functie `False`.

## Hoe je het script uitvoert

Volg deze stappen om het `palindroom_checker.py` script te gebruiken:

1.  **Sla het bestand op**: Kopieer de code hierboven en sla deze op als `palindroom_checker.py` op je computer.
2.  **Open een terminal of commandoregel**: Navigeer naar de map waarin je het bestand hebt opgeslagen.
3.  **Voer het script uit**: Typ het volgende commando en druk op Enter:
    ```bash
    python palindroom_checker.py
    ```
4.  **Voer woorden in**: Het programma vraagt je om een woord of zin in te voeren. Typ je tekst en druk op Enter.
5.  **Resultaat**: Het script laat je direct weten of je invoer een palindroom is of niet.
6.  **Afsluiten**: Om het programma af te sluiten, typ je `stop` en druk je op Enter.
