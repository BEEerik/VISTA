## 16 Vermenigvuldigen

# OPDRACHT
Vraag de gebruiker om 2 getallen in te voeren.
Gebruik een functie om het product uit te rekenen.
Toon het resultaat van de functie op het scherm.
De functie zelf mag dus niets op het scherm plaatsen.

### Vermenigvuldigen

Dit script vraagt de gebruiker om twee getallen in te voeren, berekent het product van deze getallen met behulp van een functie, en toont het resultaat op het scherm.

```python
def vermenigvuldig(getal1, getal2):
    return getal1 * getal2

getal1 = int(input("Geef een getal: "))
getal2 = int(input("Geef nog een getal: "))

resultaat = vermenigvuldig(getal1, getal2)
print(f"Het product van {getal1} en {getal2} is {resultaat}.")
```

**Uitleg:**

1. `def vermenigvuldig(getal1, getal2):`: Definieert een functie `vermenigvuldig` die twee parameters `getal1` en `getal2` accepteert.

2. `return getal1 * getal2`: De functie berekent het product van `getal1` en `getal2` en retourneert dit resultaat.

3. `getal1 = int(input("Geef een getal: "))`: Vraagt de gebruiker om een getal in te voeren en zet deze invoer om naar een integer. Dit getal wordt opgeslagen in de variabele `getal1`.

4. `getal2 = int(input("Geef nog een getal: "))`: Vraagt de gebruiker om nog een getal in te voeren en zet deze invoer om naar een integer. Dit getal wordt opgeslagen in de variabele `getal2`.

5. `resultaat = vermenigvuldig(getal1, getal2)`: Roept de functie `vermenigvuldig` aan met `getal1` en `getal2` als argumenten en slaat het geretourneerde product op in de variabele `resultaat`.

6. `print(f"Het product van {getal1} en {getal2} is {resultaat}.")`: Print het resultaat van de vermenigvuldiging op het scherm in een geformatteerde string.

Dit script helpt de gebruiker om het product van twee ingevoerde getallen te berekenen en het resultaat weer te geven.
