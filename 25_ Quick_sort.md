# Uitleg: Quick Sort Algoritme in Python

Dit document beschrijft de **Quick Sort** sorteermethode en de implementatie ervan in het Python-bestand `quick_sort.py`. Quick Sort is een van de meest efficiënte sorteeralgoritmen en werkt volgens het "verdeel en heers" principe.

## Wat is Quick Sort?

Quick Sort is een **vergelijkingssorteeralgoritme** dat een lijst of array sorteert door deze herhaaldelijk te verdelen in kleinere sub-arrays en deze vervolgens onafhankelijk te sorteren.

De kernstappen zijn:

1.  **Kies een Pivot**: Selecteer een element uit de array, de zogenaamde **pivot**. Dit is het draaipunt waar de rest van de elementen omheen wordt geordend. In de meegeleverde code kiezen we de laatste element van de lijst als pivot.
2.  **Partitioneer de Array**: Herschik de elementen in de array zo dat:
    * Alle elementen die **kleiner** zijn dan de pivot aan de **linkerkant** van de pivot komen te staan.
    * Alle elementen die **groter** zijn dan de pivot aan de **rechterkant** van de pivot komen te staan.
    * Elementen die **gelijk** zijn aan de pivot kunnen aan beide zijden terechtkomen, of, zoals in onze implementatie, in een aparte `gelijk`-lijst worden verzameld.
    Na deze stap staat de pivot op zijn definitieve, correcte positie in de gesorteerde array.
3.  **Recursieve Sortering**: Pas Quick Sort **recursief** toe op de sub-array van elementen kleiner dan de pivot en op de sub-array van elementen groter dan de pivot. Dit proces herhaalt zich totdat alle sub-arrays gesorteerd zijn. Het basisgeval voor de recursie is een array met nul of één element, die per definitie al gesorteerd is.

## Hoe het `quick_sort.py` script werkt

Het Python-script `quick_sort.py` definieert één functie: `quick_sort(arr)`.

* **Basisgeval (`if len(arr) <= 1: return arr`)**: Als de invoerlijst leeg is of slechts één element bevat, is deze al gesorteerd, en wordt de lijst direct geretourneerd. Dit is essentieel om de recursie te beëindigen.
* **Pivotkeuze (`pivot = arr[-1]`)**: In deze implementatie wordt het **laatste element** van de lijst gekozen als de pivot. Er zijn ook andere strategieën mogelijk (bijvoorbeeld het eerste element, een willekeurig element, of het mediaan van drie elementen), die elk invloed kunnen hebben op de prestaties in specifieke scenario's.
* **Partitionering (`for x in arr: ...`)**: De code itereert door alle elementen in de invoerlijst (`arr`). Elk element `x` wordt vergeleken met de `pivot`:
    * Als `x` kleiner is dan de `pivot`, wordt het toegevoegd aan de `kleiner`-lijst.
    * Als `x` gelijk is aan de `pivot`, wordt het toegevoegd aan de `gelijk`-lijst.
    * Als `x` groter is dan de `pivot`, wordt het toegevoegd aan de `groter`-lijst.
* **Recursieve oproep en samenvoeging (`return quick_sort(kleiner) + gelijk + quick_sort(groter)`)**: Dit is de kern van de recursie.
    * De `quick_sort`-functie wordt opnieuw aangeroepen voor de `kleiner`-lijst, die dan gesorteerd wordt.
    * De `quick_sort`-functie wordt opnieuw aangeroepen voor de `groter`-lijst, die dan gesorteerd wordt.
    * De uiteindelijk gesorteerde `kleiner`-lijst, gevolgd door de `gelijk`-lijst, en dan de gesorteerde `groter`-lijst, worden samengevoegd en geretourneerd als het eindresultaat.

## Hoe je het script uitvoert

Volg deze stappen om het `quick_sort.py` script te gebruiken:

1.  **Sla het bestand op**: Kopieer de code hierboven en sla deze op als `quick_sort.py` op je computer.
2.  **Open een terminal of commandoregel**: Navigeer naar de map waarin je het bestand hebt opgeslagen.
3.  **Voer het script uit**: Typ het volgende commando en druk op Enter:
    ```bash
    python quick_sort.py
    ```
4.  **Bekijk de output**: Het script zal de ongeordende lijst(en) afdrukken en vervolgens de gesorteerde versie(s) ervan tonen, wat de werking van de Quick Sort methode demonstreert.
