verlanglijst = []

while True:
    item = input("Wat zou je graag van Sinterklaas willen hebben? (typ 'KLAAR!' om te stoppen): ")
    if item.upper() == "KLAAR!":
        break
    verlanglijst.append(item)

verlanglijst.sort()

print("Je verlanglijst in alfabetische volgorde:")
for item in verlanglijst:
    print(item)

while True:
    again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
        break
    elif again in ['ja', 'j']:
        verlanglijst = []
        while True:
            item = input("Wat zou je graag van Sinterklaas willen hebben? (typ 'KLAAR!' om te stoppen): ")
            if item.upper() == "KLAAR!":
                break
            verlanglijst.append(item)

        verlanglijst.sort()

        print("Je verlanglijst in alfabetische volgorde:")
        for item in verlanglijst:
            print(item)
    else:
        print("Ongeldige invoer, probeer het opnieuw.")
