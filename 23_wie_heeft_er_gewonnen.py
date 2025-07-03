"""23 Wie heeft er gewonnen?
Vraag hoeveel spelers er zijn. 
Afhankelijk van het aantal spelers vraag je per speler de naam en de score. 
Laat op het scherm zien wie er gewonnen heeft. Hoogste score wint."""

aantal_spelers = int(input("Hoeveel spelers doen er mee? "))

namen = []
scores = []

for i in range(aantal_spelers):
    naam = input(f"Naam van speler {i+1}: ")
    score = int(input(f"Score van {naam}: "))
    namen.append(naam)
    scores.append(score)

max_score = max(scores)
winnaars = [namen[i] for i, s in enumerate(scores) if s == max_score]

if len(winnaars) == 1:
    print(f"{winnaars[0]} heeft gewonnen met {max_score} punten!")
else:
    print(f"Gelijkspel! De winnaars zijn: {', '.join(winnaars)} met {max_score} punten!")          
          