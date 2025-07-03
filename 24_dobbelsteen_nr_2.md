# Uitleg: Dobbelsteen Simulator met 'AdX' Formaat

Dit document legt het Python-script `dobbelsteen_simulator.py` uit. Dit script simuleert het gooien van verschillende soorten dobbelstenen en berekent de som van de worpen. De specificatie van de dobbelstenen gebeurt via de standaard **'AdX' notatie**, die veel wordt gebruikt in rollenspellen.

## Het 'AdX' Formaat

De 'AdX' notatie is heel eenvoudig:

* **A**: Staat voor het **aantal** dobbelstenen dat je wilt gooien.
* **d**: Dit is een vaste letter en scheidt het aantal dobbelstenen van het aantal zijden.
* **X**: Staat voor het **aantal zijden** dat elke dobbelsteen heeft.

**Voorbeelden:**

* `1d6`: Gooi één 6-zijdige dobbelsteen.
* `2d10`: Gooi twee 10-zijdige dobbelstenen.
* `3d4`: Gooi drie 4-zijdige dobbelstenen.

## Hoe het script werkt

Het `dobbelsteen_simulator.py` script gebruikt de functie `gooi_dobbelstenen(invoer_string)` om de worpen te verwerken:

1.  **Invoer verwerking**: De functie neemt een string als invoer (bijv. "2d6"). Deze wordt omgezet naar kleine letters en eventuele spaties worden verwijderd om de verwerking makkelijker te maken.
2.  **Formaatvalidatie**:
    * Het script controleert of de letter 'd' aanwezig is in de invoer. Zo niet, dan is het formaat incorrect.
    * De invoer wordt gesplitst bij de 'd' om het aantal dobbelstenen (`A`) en het aantal zijden (`X`) te isoleren.
    * Vervolgens wordt geprobeerd deze delen om te zetten naar gehele getallen. Als dit niet lukt (bijvoorbeeld als er letters staan waar cijfers moeten zijn), wordt een foutmelding gegeven.
    * Er wordt ook gecontroleerd of het aantal dobbelstenen positief is (minstens 1) en of het aantal zijden minstens 2 is (een dobbelsteen met 1 zijde is niet logisch).
3.  **Dobbelstenen gooien**: Als de invoer correct is, wordt een lus gestart die net zo vaak loopt als het opgegeven aantal dobbelstenen. In elke iteratie:
    * `random.randint(1, zijden)` wordt gebruikt om een willekeurig getal te genereren tussen 1 en het maximale aantal zijden van de dobbelsteen.
    * Dit resultaat wordt toegevoegd aan een lijst met `resultaten`.
4.  **Som berekenen**: Na alle worpen wordt de som van alle resultaten in de lijst berekend en teruggegeven.
5.  **Foutafhandeling**: Als er ergens een fout optreedt in de invoer of de verwerking, retourneert de functie een specifieke foutmelding en geeft het aan dat de operatie niet succesvol was.

## Hoe je het script uitvoert

Volg deze stappen om de `dobbelsteen_simulator.py` te gebruiken:

1.  **Sla het bestand op**: Kopieer de code hierboven en sla deze op als `dobbelsteen_simulator.py` op je computer.
2.  **Open een terminal of commandoregel**: Navigeer naar de map waarin je het bestand hebt opgeslagen.
3.  **Voer het script uit**: Typ het volgende commando en druk op Enter:
    ```bash
    python dobbelsteen_simulator.py
    ```
4.  **Voer dobbelsteenformaten in**: Het programma vraagt je om het type dobbelstenen in te voeren (bijv. `1d6`, `2d10`, `3d4`). Typ je invoer en druk op Enter.
5.  **Resultaat**: Het script berekent de som van de worpen en toont deze. Bij incorrecte invoer krijg je een foutmelding.
6.  **Afsluiten**: Om het programma af te sluiten, typ je `stop` en druk je op Enter.