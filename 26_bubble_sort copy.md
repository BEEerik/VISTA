# Uitleg: Bubble Sort Algoritme in Python

Dit document beschrijft de **Bubble Sort** methode en de implementatie ervan in het Python-bestand `bubble_sort.py`. Bubble Sort is een eenvoudig sorteeralgoritme dat elementen herhaaldelijk vergelijkt en omwisselt totdat de lijst gesorteerd is.

## Wat is Bubble Sort?

Bubble Sort is een van de meest elementaire sorteeralgoritmen. Het werkt door **aangrenzende elementen** in een lijst herhaaldelijk te vergelijken en ze van positie te wisselen als ze in de verkeerde volgorde staan. Dit proces wordt voortgezet totdat er een volledige doorgang door de lijst plaatsvindt zonder enige omwisselingen, wat aangeeft dat de lijst nu gesorteerd is. De naam "Bubble Sort" komt voort uit het idee dat de grootste (of kleinste, afhankelijk van de sorteerrichting) elementen langzaam naar hun juiste positie aan het einde (of begin) van de lijst "omhoog borrelen", net als bellen in een vloeistof.

### Kernstappen:

1.  **Vergelijk Aangrenzende Elementen**: Het algoritme begint bij het eerste element van de lijst en vergelijkt het met het direct daaropvolgende element.
2.  **Wissel indien Nodig**: Als de elementen niet in de gewenste volgorde staan (bijv. het eerste is groter dan het tweede bij oplopend sorteren), worden ze van plaats gewisseld.
3.  **Herhaal voor de Hele Lijst**: Dit proces van vergelijken en omwisselen wordt voortgezet voor elk paar aangrenzende elementen in de lijst tot het einde is bereikt.
4.  **Grootste Element op zijn Plaats**: Na één volledige "pass" (doorgang) is het grootste element (of kleinste) gegarandeerd op zijn uiteindelijke, correcte positie aan het einde van het (nog ongeordende) deel van de lijst.
5.  **Minder Vergelijkingen**: Bij elke volgende pass hoeft het algoritme niet meer de reeds gesorteerde elementen aan het einde van de lijst te controleren, wat de te doorlopen sectie telkens kleiner maakt.
6.  **Stopconditie**: Het sorteren stopt wanneer er in een complete pass geen enkele omwisseling heeft plaatsgevonden. Dit betekent dat alle elementen al op hun juiste plek staan en de lijst gesorteerd is.

## Hoe het `bubble_sort.py` script werkt

Het Python-script `bubble_sort.py` definieert één functie: `bubble_sort(arr)`.

* **`n = len(arr)`**: Haalt de lengte van de lijst op, die nodig is voor de lussen.
* **Buitenste lus (`for i in range(n):`)**: Deze lus controleert het aantal passes dat nodig is. Na elke pass staat minstens één element op zijn definitieve gesorteerde positie aan het einde van het ongeordende segment van de lijst. `i` representeert het aantal elementen aan het einde dat al gesorteerd is.
* **`swapped = False`**: Deze boolean-vlag wordt aan het begin van elke pass gereset. Als na een volledige innerlijke lus (een pass) `swapped` nog steeds `False` is, betekent dit dat er geen omwisselingen zijn geweest, wat aangeeft dat de lijst al gesorteerd is.
* **Binnenste lus (`for j in range(0, n - i - 1):`)**: Deze lus itereert door het ongeordende deel van de lijst. De `- i - 1` zorgt ervoor dat we niet verder gaan dan de elementen die al gesorteerd zijn aan het einde.
* **Vergelijking en omwisseling (`if arr[j] > arr[j + 1]:`)**:
    * Als het huidige element (`arr[j]`) groter is dan het volgende element (`arr[j + 1]`), zijn ze in de verkeerde volgorde (voor oplopend sorteren).
    * Ze worden omgewisseld (`arr[j], arr[j + 1] = arr[j + 1], arr[j]`).
    * De `swapped` vlag wordt op `True` gezet, wat aangeeft dat er een omwisseling heeft plaatsgevonden in deze pass.
* **Vroegtijdige stop (`if not swapped: break`)**: Als de innerlijke lus eindigt en `swapped` is nog steeds `False`, betekent dit dat er in de hele pass geen elementen zijn omgewisseld. De lijst is dus gesorteerd, en we kunnen het sorteerproces vroegtijdig beëindigen.

## Hoe je het script uitvoert

Volg deze stappen om het `bubble_sort.py` script te gebruiken:

1.  **Sla het bestand op**: Kopieer de code hierboven en sla deze op als `bubble_sort.py` in de map die je hebt aangemaakt (bijv. `PythonSortVoorbeelden`).
2.  **Open een terminal of commandoregel**:
    * **Windows**: Typ `cmd` in de zoekbalk van het Startmenu en druk op Enter.
    * **macOS**: Ga naar `Programma's` > `Hulpprogramma's` > `Terminal`.
    * **Linux**: Open je terminal-applicatie.
3.  **Navigeer naar de map**: Gebruik het `cd` commando (change directory) om naar de map te gaan waar je het `bubble_sort.py` bestand hebt opgeslagen. Bijvoorbeeld, als je het in een map genaamd `PythonSortVoorbeelden` in je `Documenten` hebt opgeslagen:
    ```bash
    cd C:\Users\JouwGebruikersnaam\Documents\PythonSortVoorbeelden
    # Of voor macOS/Linux:
    # cd ~/Documents/PythonSortVoorbeelden
    ```
    (Vervang `JouwGebruikersnaam` met je daadwerkelijke gebruikersnaam).
4.  **Voer het script uit**: Typ het volgende commando en druk op Enter:
    ```bash
    python bubble_sort.py
    ```
5.  **Bekijk de output**: Het script zal de ongeordende lijsten afdrukken en vervolgens de gesorteerde versies ervan tonen, wat de werking van de Bubble Sort methode demonstreert.
