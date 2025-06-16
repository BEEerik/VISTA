
""""
20
Lootbox
Maak een programma dat een loot drop simuleert. 
Common, Uncommon, Rare, Epic en Legendary zijn de verschillende niveaus qua loot,
op volgorde van wat het meest voorkomt tot wat het minst voorkomt. 
Zorg ervoor dat jouw programma hier rekening mee houdt.
"""

import random

def loot_drop():
    loot_niveaus = {
        "Common": 0.6,    # 60% kans
        "Uncommon": 0.25, # 25% kans
        "Rare": 0.1,      # 10% kans
        "Epic": 0.04,     # 4% kans
        "Legendary": 0.01 # 1% kans
    }

    # Kies een loot-niveau 
    loot = random.choices(list(loot_niveaus.keys()), list(loot_niveaus.values()))[0]
    return loot

# Simuleer loot drop
loot = loot_drop()
print(f"Je hebt een {loot} item gekregen!")
