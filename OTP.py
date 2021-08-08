import random

dateityplist = ["txt", "pdf", "mp3"]
textstring = ""
schluessellist = []
schluesselstring = ""
textlist = []

print("Wollen Sie entschlüsseln oder verschlüsseln?")
#entoderverschluesslung = input("(e)ntschlüssen oder (v)erschlüsseln: ")
entoderverschluesslung = "v"
entoderverschluesslung = entoderverschluesslung.lower()
if entoderverschluesslung == "v":
    while True:
        print("Was für einen Dateitypen wollen Sie in eine OTP Datei umwandeln?")
        dateityp = input("txt, pdf, jpg, mp3: ")
        dateityp = dateityp.lower()
        if dateityp not in dateityplist:
            print("Unglültige Dateiendung. Versuchen Sie es erneut.")
        if dateityp in dateityplist:
            print("Die Eingabe war gültig. Ausgewählter Dateityp: "+ dateityp)
            break

    while True:
        # filepath = input("Geben Sie nun bitte den Dateipfad an: ")
        filepath = "/Users/philippbecker/Desktop/ptext.txt"
        print("Es wird geprüft, ob der Dateityp des Pfades gleich der Ausgewählten Dateiendung ist.")
        last3digits = str(filepath[-1]+filepath[-2]+filepath[-3])
        print(last3digits+" Sind die letzten 3 Buchstaben des Eingegebenen Pfades.")
        if last3digits != dateityp:
            print("Die Eingegebene Datei Endung war nicht korrekt.")
        if last3digits == dateityp:
            print("Die von ihnen Eingegebene Datei Endung war korrekt")
            break
    if dateityp == "txt":
        text = open(filepath, "r")
        textstring=(text.read())
    print(textstring)
    textbytes = "".join(format(ord(x), 'b') for x in textstring)
    print(textbytes)
    indexbytes = 0
    while(indexbytes<len(textbytes)):
        textlist.append(int(textbytes[indexbytes]))
        indexbytes+=1
    print(textlist)
    while True:
        schluesseljanein = input("Haben Sie bereits einen Schlüssel? Wenn ja (j), wenn nein (n) eingeben: ")
        if schluesseljanein == "n":
            indexlist = 0
            while(indexlist<len(textbytes)):
                schluessellist.append(random.randint(0,1))
                indexlist+=1
            print(schluessellist, "Dies ist ihr Schlüssel in einer Liste")
            for i in range(0,len(textbytes)):
                schluesselstring+=(str(schluessellist[i]))
            print(schluesselstring+" dies ist ihr Schlüssel in Plain Text")
            break

        if schluesseljanein == "j":
            schluesselja = input("Bitte geben Sie hier Ihren Plain Text Schlüssel ein: ")
            indexja = 0
            while(indexja<len(schluesselja)):
                schluessellist.append(int(schluesselja[indexja]))
                indexja+=1
            print(schluessellist)
            break

        if schluesseljanein != "j" or "n":
            print("Überprüfen Sie Ihre Eingaben")









if entoderverschluesslung == "e":
    print("Die Verschlüsslung wird durchgeführt")











