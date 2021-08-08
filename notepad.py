filepath = input("Bitte geben Sie den Dateipfad des Note Dokuemnts an: ")
while True:
    mode = input("Möchten Sie ein Ereignis hinzufügen (a) ihre jetzigen ansehen(v) ein neues Register erstellen (n) oder ein Register löschen (d)?: ")
    if mode.lower() == "n":
        print("Ein neues Register wird erstellt...")
        registername = input("Wie soll das neue Register heißen?: ")
        break
    else:
        print("Bitte überprüfen Sie Ihre Eingaben")