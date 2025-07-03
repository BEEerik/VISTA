while True:
    getal_1 = float(input("Eerste getal? "))
    operator = input("Welke Operator wil je gebruiken? ")
    getal_2 = float(input("Tweede getal? "))

    if operator == "+":
        print(f"De uitkomst is: {getal_1 + getal_2}")
    elif operator == "-":
        print(f"De uitkomst is: {getal_1 - getal_2}")
    elif operator == "*":
        print(f"De uitkomst is: {getal_1 * getal_2}")
    elif operator == "/":
        print(f"De uitkomst is: {getal_1 / getal_2}")
    else:
        print("Operator niet herkend")
    
    again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
        break

# uitleg https://youtu.be/eaFyMkTz7aM