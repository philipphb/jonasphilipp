maxzahl = 100
primzahl = []
for zahl in range(2,maxzahl):
    print(zahl)
    for teiler in range(zahl,maxzahl):
        print(teiler)
        if(zahl%teiler==0 and zahl!=teiler and ):
            primzahl.append(zahl)