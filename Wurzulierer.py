import math
inpuzahl = input("Von welcher Zahl soll die Wurzel berechnet werden?: ")
#inpuzahl = 4
inpuzahl = int(inpuzahl)
zahlzahlhochminuszahl = (inpuzahl-((inpuzahl*inpuzahl)**-inpuzahl))

for testzahl in range(0,inpuzahl,(inpuzahl*inpuzahl)):
    zahl = float(testzahl)
    if(testzahl*testzahl==inpuzahl):
        print("Die Algorithmus Funktion hat eine Wurzel von: "+str(testzahl)+" herausgefunden.")
        break
    if((testzahl*testzahl)<(inpuzahl-((inpuzahl*inpuzahl)**-10))):
        print("Die Algorithmus Funktion hat eine Wurzel von: "+str(testzahl) + " herausgefunden.")
        break
    if((testzahl*testzahl>(inpuzahl+((inpuzahl*inpuzahl)**-10)))):
        print("Die Algorithmus Funktion hat eine Wurzel von: "+str(testzahl) + " herausgefunden.")
        break
print("Die math Funktion hat einen Wert von: "+str(math.sqrt(inpuzahl))+" herausgefunden")