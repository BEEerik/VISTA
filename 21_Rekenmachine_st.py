from shared import float_input
import math

# Not a Number  = NaN
# Infinity      = inf
# Negative      = -inf

value = float_input("Geef een getal: ")

print(f"is NaN: {math.isnan(value)}")
print(f"is Infinity: {math.isinf(value)}")
print(f"is Negative: {value < 0}")



""" 21 Rekenmachine
De rekenmachine vraagt de gebruiker om een getal. 
Vervolgens wordt gevraagd welke actie er uitgevoerd moet worden. 
De acties zijn: + (plus), - (minus), / (delen), * (vermenigvuldigen), = (uitkomst). 
Als de actie 'uitkomst' gekozen wordt, toont het programma het resultaat op het scherm. 
Als een andere actie gekozen wordt, dan wordt er om een nieuw getal gevraagd om deze actie mee uit te voeren.

Simon > Erik
nog nodig van Simon: Shared.py en sest.py
"""


