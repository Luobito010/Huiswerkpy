coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1]  # Lijst van muntwaarden, van groot naar klein
toPay = int(float(input('Amount to pay: ')) * 100)  # Bedrag dat betaald moet worden, omgezet naar centen
paid = int(float(input('Paid amount: ')) * 100)     # Betaald bedrag, ook omgezet naar centen
change = paid - toPay                                # Het wisselgeld dat teruggegeven moet worden
returnedCoins = {}  # Dictionary om bij te houden hoeveel munten van elke soort zijn teruggegeven
while change > 0 and len(coinValues) > 0:           # Zolang er wisselgeld over is en er nog muntwaarden zijn
    coinValue = coinValues.pop(0)                    # Neem de grootste muntwaarde uit de lijst (pop(0) haalt eerste element)
    nrCoins = change // coinValue                    # Bereken maximaal aantal munten van deze waarde dat kan worden teruggegeven
    if nrCoins > 0:                                  # Als er munten van deze waarde teruggegeven kunnen worden
        print('Return maximal', nrCoins, 'coins of', coinValue, 'cents!')  # Toon maximale aantal munten
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? '))  # Vraag gebruiker hoeveel munten daadwerkelijk teruggegeven zijn
        change -= nrCoinsReturned * coinValue       # Verminder het wisselgeld met het teruggegeven bedrag
        # Sla het aantal teruggegeven munten op in de dictionary
        if coinValue in returnedCoins:
            returnedCoins[coinValue] += nrCoinsReturned
        else:
            returnedCoins[coinValue] = nrCoinsReturned
if change > 0:                                       # Als er na alle munten nog wisselgeld over is
    print('Change not returned:', str(change) + ' cents')  # Meld dat niet al het wisselgeld is teruggegeven
else:
    print('Done, all change returned!')             # Meld dat het wisselgeld volledig is teruggegeven
# Print overzicht van alle teruggegeven muntstukken
print('\nOverzicht van teruggegeven munten:')
for coin in sorted(returnedCoins.keys(), reverse=True):  # Sorteer munten van groot naar klein
    print(f"{returnedCoins[coin]} munt(en) van {coin} cent")
