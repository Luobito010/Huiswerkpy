
juiste_wachtwoord = "juistewachtwoord"

max_pogingen = 5

pogingen = 0

while pogingen < max_pogingen:
    invoer = input("voer je wachtwoord in: ")
    pogingen += 1
    if invoer == juiste_wachtwoord:
     print(f"Juist je hebt het wachtwoord in {pogingen} pogingen")
     break
else:
    print("je hebt de maximale pogingen bereikt probeer het later nog een keer.")