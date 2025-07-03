def bubble_sort(arr):
    """
    Implementeert de Bubble Sort sorteermethode.
    Sorteert een lijst in oplopende volgorde.
    """
    n = len(arr)
    # Loop door alle elementen van de array
    for i in range(n):
        # Vlag om te controleren of er een omwisseling heeft plaatsgevonden
        # Als er geen omwisselingen zijn in een doorgang, is de lijst gesorteerd
        swapped = False

        # Laatste i elementen zijn al op hun plaats, dus we hoeven ze niet meer te controleren
        for j in range(0, n - i - 1):
            # Vergelijk aangrenzende elementen
            if arr[j] > arr[j + 1]:
                # Wissel om als ze in de verkeerde volgorde staan
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Als er geen twee elementen zijn omgewisseld door de innerlijke lus,
        # dan is de lijst gesorteerd en kunnen we vroegtijdig stoppen
        if not swapped:
            break
    return arr

# Voorbeeld van gebruik
if __name__ == "__main__":
    ongeordende_lijst_1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Ongeordende lijst 1: {ongeordende_lijst_1}")
    gesorteerde_lijst_1 = bubble_sort(ongeordende_lijst_1)
    print(f"Gesorteerde lijst 1: {gesorteerde_lijst_1}")

    print("\n--- Test met een andere lijst ---")
    ongeordende_lijst_2 = [5, 1, 4, 2, 8]
    print(f"Ongeordende lijst 2: {ongeordende_lijst_2}")
    gesorteerde_lijst_2 = bubble_sort(ongeordende_lijst_2)
    print(f"Gesorteerde lijst 2: {gesorteerde_lijst_2}")

    print("\n--- Test met al gesorteerde lijst ---")
    ongeordende_lijst_3 = [1, 2, 3, 4, 5]
    print(f"Ongeordende lijst 3: {ongeordende_lijst_3}")
    gesorteerde_lijst_3 = bubble_sort(ongeordende_lijst_3)
    print(f"Gesorteerde lijst 3: {gesorteerde_lijst_3}")

    print("\n--- Test met omgekeerde lijst ---")
    ongeordende_lijst_4 = [5, 4, 3, 2, 1]
    print(f"Ongeordende lijst 4: {ongeordende_lijst_4}")
    gesorteerde_lijst_4 = bubble_sort(ongeordende_lijst_4)
    print(f"Gesorteerde lijst 4: {gesorteerde_lijst_4}")