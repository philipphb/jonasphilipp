kontostand = input("Wie hoch ist der Betrag auf ihrem Konto?: ")
abbuchung = input("Wie viel wollen Sie abbuchen?:")
kontostand = int(kontostand)
abbuchung = int(abbuchung)
while True:
    if((kontostand-abbuchung)>=0):
        kontostand = kontostand-abbuchung
        print("Es wurden"+str(abbuchung)+"von ihrem Konto abgebucht. Es befinden sich nun noch"+str(kontostand)+"€ auf ihrem Konto")
        break
    if((kontostand-abbuchung)<0):
        print("Auf ihrem Konto ist zu wenig Geld. Sie wollen"+str(abbuchung)+"€ Abbuchen, haben aber nur"+str(kontostand)+"€ auf Ihrem Konto.")
        break