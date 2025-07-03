BtwPercentage = 21

BedragZonderBtw = input("Voer een bedrag zonder BTW in: ")

BedragMetBtw = float(BedragZonderBtw) * (1 + BtwPercentage / 100)
print (f"het bedrag met {BtwPercentage}% BTW is: {BedragMetBtw}")


"""
03 BTW
Vraag de gebruiker om een bedrag zonder BTW in te vullen. 
Bereken het bedrag met BTW (21%) en print deze op scherm.
"""

""""
BtwPercentage = 21

BedragZonderBtw = input("Voer een bedrag zonder BTW in: ")

# Bereken het BTW-bedrag
BtwBedrag = float(BedragZonderBtw) * (BtwPercentage / 100)

# Bereken het totaalbedrag inclusief BTW
BedragMetBtw = float(BedragZonderBtw) + BtwBedrag

print(f"Het bedrag zonder BTW is: {BedragZonderBtw}")
print(f"De BTW ({BtwPercentage}%) is: {BtwBedrag}")
print(f"Het bedrag met {BtwPercentage}% BTW is: {BedragMetBtw}")
""""
