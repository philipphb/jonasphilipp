from termcolor import cprint

primzahllist = []
maxzahllist = []
vielfachlist = []
while True:
    cprint("Ihre Eingabe muss größer >=2 sein und darf keine Kommastellen enthalten.",'yellow')
    cprint("Wenn Ihre Eingabe doch eine Kommazahl ist, dann wird diese Zahl automatisch gerundet.",'yellow')
    maxzahl = input("Bis zu welcher Zahl soll eine Primzahl berechnet werden?: ")
    maxzahl = float(maxzahl)
    maxzahl = round(maxzahl)
    if(maxzahl>=2):
        print("Die Eingabe war gültig.")
        print("Berechnung wird gestartet")
        break
    else:
        print("Die Zahl muss größer 1 sein. Ungültige Eingabe.")


for zahelnreihe in range(2,maxzahl+1):
    maxzahllist.append(zahelnreihe)
    cprint(("Liste wird gefüllt mit Werten ... momentan bei zahlenreihe =",zahelnreihe),'yellow')
cprint(("maxzahllist wurde mit insgesamt "+str(len(maxzahllist))+" Werten gefüllt."),'green')


index = 0
while(index<len(maxzahllist)):
    primzahllist.append(maxzahllist[0])
    zahl = int(maxzahllist[0])
    cprint(("Der Löscungsprozess ist momentan bei index: "+str(index)),'green')
    cprint(("Primzahl: "+str(zahl)),'red')
    print("Done")
    for loeschen in range(2,len(maxzahllist)):
        cprint(("for loeschen ist bei: "+str(loeschen)),'green')
        if(loeschen%zahl==0):
            item = maxzahllist.index(loeschen)
            maxzahllist.remove(loeschen)
            cprint(("Die if Löschung is bei: "+str(loeschen)),'green')
    index+=1


print("max"+maxzahllist)
print("prim"+primzahllist)



cprint("Done!",'green')
cprint(primzahllist,'yellow')
primzahllist = str(maxzahllist)
text_file = open("/Users/philippbecker/Desktop/primzahlist.txt", "w")
text_file.write(primzahllist)
text_file.close()
