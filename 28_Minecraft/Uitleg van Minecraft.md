# Uitleg van Minecraft.py

Dit Python-script leest een JSON-bestand in, past bepaalde eigenschappen aan en slaat de aangepaste gegevens op in een nieuw JSON-bestand. Hieronder volgt een stap-voor-stap uitleg van de code.

## Importeren van de JSON-module

```python
import json
```

De json-module wordt geïmporteerd om te kunnen werken met JSON-bestanden.

## Stap 1: Lees het JSON-bestand in

```python
with open('gras_blok.json', 'r') as file:
    blok_data = json.load(file)
```

* Het JSON-bestand gras_blok.json wordt geopend in leesmodus ('r').
* De inhoud van het bestand wordt gelezen en omgezet in een Python-dictionary (blok_data) met behulp van json.load(file).

## Stap 2: Pas de eigenschappen aan

```python
blok_data['snow'] = True
blok_data['y'] += 66
blok_data['z'] *= 3
```

* De eigenschap snow wordt ingesteld op True.
* De y-coördinaat wordt verhoogd met 66.
* De z-coördinaat wordt vermenigvuldigd met 3.

## Stap 3: Sla de aangepaste dictionary op als een nieuw JSON-bestand

```python
with open('sneeuw_blok.json', 'w') as file:
    json.dump(blok_data, file, indent=4)
print("De eigenschappen zijn aangepast en opgeslagen in sneeuw_blok.json")
```

* Een nieuw JSON-bestand genaamd sneeuw_blok.json wordt geopend in schrijfmodus ('w'). Als het bestand nog niet bestaat, wordt het aangemaakt. Als het bestand al bestaat, wordt de inhoud ervan overschreven.
* De aangepaste gegevens (blok_data) worden geschreven naar het bestand met behulp van json.dump(blok_data, file, indent=4). De parameter indent=4 zorgt ervoor dat de JSON-inhoud netjes wordt geformatteerd met een inspringing van 4 spaties.

## Eindmelding
```python
print("De eigenschappen zijn aangepast en opgeslagen in sneeuw_blok.json")
```

* Een bericht wordt afgedrukt naar de console om aan te geven dat de eigenschappen zijn aangepast en opgeslagen in sneeuw_blok.json.
...


