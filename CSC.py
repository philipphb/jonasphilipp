import math
from tkinter import *
#import extcolors
def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'
decend = input("Wollen Sie Text Entschlüsseln (e) oder Verschlüsseln (d)?: ")
decend = decend.lower()
while(decend == "d"):
    inputtext = input("Welchen Text möchten Sie in einen PyramidScan Code (PS Code) konvertieren?: ")
    textlenght = int(len(inputtext))
    while(textlenght < 30):
        if(textlenght > 30):
            print("Der Text ist leider zu lang")
        print(inputtext, "wird in einen PS Code umgewandelt...")

        wurzeltextlen = math.ceil(math.sqrt(textlenght))
        print("Ein",wurzeltextlen,"x",wurzeltextlen,"Felder großes Rechteck wird komprimiert...")
        print(textlenght,"Stellen langer Text wird in einen PS Code transkribiert...")
        variabelstelle = "variabelstelle"
        stellenvariabelindex = 0
        stellenliste = []
        while(stellenvariabelindex < textlenght):
            stellenliste.insert(stellenvariabelindex, (inputtext[stellenvariabelindex]).lower())
            stellenvariabelindex = stellenvariabelindex+1
        print(stellenliste," wird konvertiert...")
        stellenrgblistindex = 0
        stellenrgblist = []
        while(stellenrgblistindex < (textlenght)):
            if(str(stellenliste[stellenrgblistindex]) == "a"):
                stellenrgblist.insert(stellenrgblistindex,str((rgbtohex(r=stellenrgblistindex+10,g=0,b=0))))
            if (str(stellenliste[stellenrgblistindex]) == "b"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=10, b=10))))
            if (str(stellenliste[stellenrgblistindex]) == "c"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=20, b=20))))
            if (str(stellenliste[stellenrgblistindex]) == "d"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=30, b=30))))
            if (str(stellenliste[stellenrgblistindex]) == "e"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=40, b=40))))
            if (str(stellenliste[stellenrgblistindex]) == "f"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=50, b=50))))
            if (str(stellenliste[stellenrgblistindex]) == "g"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=60, b=60))))
            if (str(stellenliste[stellenrgblistindex]) == "h"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=70, b=70))))
            if (str(stellenliste[stellenrgblistindex]) == "i"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=80, b=80))))
            if (str(stellenliste[stellenrgblistindex]) == "j"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=90, b=90))))
            if (str(stellenliste[stellenrgblistindex]) == "k"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=100, b=100))))
            if (str(stellenliste[stellenrgblistindex]) == "l"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=110, b=110))))
            if (str(stellenliste[stellenrgblistindex]) == "m"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=120, b=120))))
            if (str(stellenliste[stellenrgblistindex]) == "n"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=130, b=130))))
            if (str(stellenliste[stellenrgblistindex]) == "o"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=140, b=140))))
            if (str(stellenliste[stellenrgblistindex]) == "p"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=150, b=150))))
            if (str(stellenliste[stellenrgblistindex]) == "q"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=160, b=160))))
            if (str(stellenliste[stellenrgblistindex]) == "r"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=170, b=170))))
            if (str(stellenliste[stellenrgblistindex]) == "s"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=180, b=180))))
            if (str(stellenliste[stellenrgblistindex]) == "t"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=190, b=190))))
            if (str(stellenliste[stellenrgblistindex]) == "u"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=200, b=200))))
            if (str(stellenliste[stellenrgblistindex]) == "v"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=210, b=210))))
            if (str(stellenliste[stellenrgblistindex]) == "w"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=220, b=220))))
            if (str(stellenliste[stellenrgblistindex]) == "x"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=230, b=230))))
            if (str(stellenliste[stellenrgblistindex]) == "y"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=240, b=240))))
            if (str(stellenliste[stellenrgblistindex]) == "z"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=250, b=250))))
            if (str(stellenliste[stellenrgblistindex]) == "."):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=15, b=35))))
            if (str(stellenliste[stellenrgblistindex]) == ":"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=25, b=45))))
            if (str(stellenliste[stellenrgblistindex]) == "/"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=35, b=55))))
            if (str(stellenliste[stellenrgblistindex]) == "ä"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=45, b=65))))
            if (str(stellenliste[stellenrgblistindex]) == "ö"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=55, b=75))))
            if (str(stellenliste[stellenrgblistindex]) == "ü"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=65, b=85))))
            if (str(stellenliste[stellenrgblistindex]) == "?"):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=75, b=95))))
            if (str(stellenliste[stellenrgblistindex]) == "="):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=85, b=105))))
            if (str(stellenliste[stellenrgblistindex]) == " "):
                stellenrgblist.insert(stellenrgblistindex, str((rgbtohex(r=stellenrgblistindex*3 + 10, g=95, b=115))))
            stellenrgblistindex = stellenrgblistindex+1

        print(stellenrgblist)
        window = Tk()
        window.title(("Pyramid Scan Code", inputtext))
        window.geometry("600x600")
        windowindex = 0
        height = wurzeltextlen
        width = wurzeltextlen

        while(windowindex < textlenght):
            square = Canvas(window, height=30, width=30, bg=stellenrgblist[windowindex])
            square.pack()
            windowindex = windowindex+1

        window.mainloop()
        window.update()
        window.postscript(file="/Users/philippbecker/Desktop/file_name.ps", colormode='color')
        window.mainloop()
if(decend == "e"):
    print("Entschlüsslung wird durchgeführt")
    #filename = input("Wie lautet der Dateipfad der Pyramid Scan Datei?: ")
    filename = "/Users/philippbecker/Documents/Programmieren/Python/CSC/tesla.png"
    print(filename)
#test
































