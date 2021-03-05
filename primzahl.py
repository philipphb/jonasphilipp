from termcolor import cprint
from math import  *

primzahllist = []
maxzahllist = []
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




print(eratosthenes(100))

cprint("Done!",'green')
cprint(primzahllist,'yellow')
primzahllist = str(primzahllist)
text_file = open("/Users/philippbecker/Desktop/primzahlist.txt", "w")
text_file.write(primzahllist)
text_file.close()
