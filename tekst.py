tekst = "hallo wereld"

vorige_teken = ""

for teken in tekst:
    if teken != vorige_teken:
        print(teken)    
        vorige_teken = teken