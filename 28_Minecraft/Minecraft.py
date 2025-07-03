import json

# Stap 1: Lees het JSON-bestand in
with open('gras_blok.json', 'r') as file:
    blok_data = json.load(file)

# Stap 2: Pas de eigenschappen aan
blok_data['snow'] = True
blok_data['y'] += 66
blok_data['z'] *= 3

# Stap 3: Sla de aangepaste dictionary op als een nieuw JSON-bestand
with open('sneeuw_blok.json', 'w') as file:
    json.dump(blok_data, file, indent=4)

print("De eigenschappen zijn aangepast en opgeslagen in sneeuw_blok.json")