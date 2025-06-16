### 14 Fibonacci 

# Uitleg Fibonacci
De Fibonacci-reeks is een getallenreeks waarbij elk getal (vanaf het derde getal) de som is van de twee voorgaande getallen. De reeks begint doorgaans met de getallen 0 en 1. Hier zijn de eerste paar getallen in de Fibonacci-reeks om een idee te geven:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Zoals je ziet, is elk getal de som van de twee vorige getallen:

Het derde getal is 0 + 1 = 1.

Het vierde getal is 1 + 1 = 2.

Het vijfde getal is 1 + 2 = 3.

Het zesde getal is 2 + 3 = 5.

En zo gaat het verder. De Fibonacci-reeks heeft veel interessante eigenschappen en komt voor in verschillende natuurverschijnselen, zoals de rangschikking van bladeren aan een stengel, de vorming van bloembladen en de verdeling van zaden in een zonnebloem.

# OPDRACHT
Schrijf een programma dat de eerste 15 getallen van de Fibonacci reeks op het scherm laat zien. Gebruik hiervoor een lus.

# Aantal getallen in Fibonacci reeks
`aantal_getallen = 15`

Deze regel stelt het aantal Fibonacci-getallen dat gegenereerd moet worden in op 15.

# Eerste twee getallen Fibonacci reeks
`fib1, fib2 = 0, 1`

Deze regel initialiseert de eerste twee getallen van de Fibonacci-reeks. `fib1` wordt ingesteld op 0 en `fib2` wordt ingesteld op 1.

`print("De eerste 15 getallen van de Fibonacci reeks zijn:")`

Deze regel print een bericht dat aangeeft dat de volgende getallen de eerste 15 getallen van de Fibonacci-reeks zijn.

# Lus om eerste 15 getallen Fibonacci reeks te maken
```
for _ in range(aantal_getallen):
    print(fib1, end=" ")
    fib1, fib2 = fib2, fib1 + fib2
```

Dit codeblok is een lus die 15 keer wordt uitgevoerd (zoals gespecificeerd door `aantal_getallen`).

`for _ in range(aantal_getallen):` creëert een lus die 15 keer herhaalt.
`print(fib1, end=" ")` print de huidige waarde van `fib1` gevolgd door een spatie, zonder naar een nieuwe regel te gaan.
`fib1, fib2 = fib2, fib1 + fib2` werkt de waarden van `fib1` en `fib2` bij voor de volgende iteratie. `fib1` neemt de waarde van `fib2`, en `fib2` neemt de waarde van `fib1 + fib2`.
Deze lus genereert en print de eerste 15 getallen van de Fibonacci-reeks.

