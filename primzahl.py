from termcolor import cprint
primzahllist = []
maxzahllist = []
colorlist = []
while True:
    #maxzahl1 = input("Bis zu welcher Zahl soll eine Primzahl berechnet werden?: ")
    maxzahl1 = 100
    maxzahl1 = int(maxzahl1)
    maxzahl = int(maxzahl1+1)
    if(maxzahl1>0):
        print("Die Eingabe war gültig.")
        print("Berechnung wird gestartet")
        break
    if(maxzahl<=0):
        print("Die Zahl muss größer 1 sein. Ungültige Eingabe.")

indexcolor = 0
while(indexcolor<maxzahl):
    colorlist.append('red',)
    cprint('red','red')
    colorlist.append('green')
    cprint('green','green')
    indexcolor+=1



indexmax = 1
while(indexmax<maxzahl):
    maxzahllist.append(indexmax)
    cprint(indexmax,colorlist[indexmax])
    indexmax+=1


indexgesamt = 0
while(indexgesamt<maxzahl):
    indexeinzel = 0
    while(indexeinzel<maxzahl):
        cprint(indexeinzel,colorlist[indexeinzel])
        if((indexeinzel/maxzahllist[indexeinzel])==1):
            primzahllist.append(indexeinzel)
        indexeinzel+=1
    indexgesamt+=1


cprint(primzahllist,'yellow')
text_file = open("/Users/philippbecker/Desktop/primzahlist.txt", "w")
text_file.write(primzahllist)
text_file.close()
