import random

def quick_sort(arr):
    """
    Implementeert de Quick Sort sorteermethode.
    """
    # Basisgeval: Een array met 0 of 1 element is al gesorteerd.
    if len(arr) <= 1:
        return arr

    # Kies de pivot: Hier kiezen we het laatste element als pivot.
    # Een willekeurige keuze kan ook helpen om het worst-case scenario te voorkomen.
    # Voor dit voorbeeld houden we het eenvoudig en kiezen we de laatste.
    pivot = arr[-1] 

    # Lijsten voor elementen kleiner dan, gelijk aan, en groter dan de pivot
    kleiner = []
    gelijk = []
    groter = []

    # Partitioneer de array
    for x in arr:
        if x < pivot:
            kleiner.append(x)
        elif x == pivot:
            gelijk.append(x)
        else: # x > pivot
            groter.append(x)

    # Recursief sorteren van de sub-arrays en samenvoegen
    return quick_sort(kleiner) + gelijk + quick_sort(groter)

# Voorbeeld van gebruik
if __name__ == "__main__":
    ongeordende_lijst = [3, 6, 8, 10, 1, 2, 1, 5, 7, 4, 9, 3]
    print(f"Ongeordende lijst: {ongeordende_lijst}")

    gesorteerde_lijst = quick_sort(ongeordende_lijst)
    print(f"Gesorteerde lijst: {gesorteerde_lijst}")

    print("\n--- Test met een andere lijst ---")
    lijst_2 = [99, 12, 54, 3, 27, 88, 1, 65, 42, 100]
    print(f"Ongeordende lijst: {lijst_2}")
    gesorteerde_lijst_2 = quick_sort(lijst_2)
    print(f"Gesorteerde lijst: {gesorteerde_lijst_2}")

    print("\n--- Test met dubbele waarden ---")
    lijst_3 = [5, 2, 8, 2, 5, 1]
    print(f"Ongeordende lijst: {lijst_3}")
    gesorteerde_lijst_3 = quick_sort(lijst_3)
    print(f"Gesorteerde lijst: {gesorteerde_lijst_3}")