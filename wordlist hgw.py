KONSONANTEN = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
konsonanten = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vokale = ["a", "e", "i", "o", "u"]
zahlen = ["0","1","2","3","4","5","6","7","8","9"]
pospswrd = []
counter = 0

txt = open("/Users/philippbecker/Desktop/wordlist.txt","w+")
#txt2 = open("/Users/philippbecker/Desktop/"+i+".txt","w+")


for i in KONSONANTEN:
    txt2 = open("/Users/philippbecker/Desktop/" + i + ".txt", "w+")
    for j in vokale:
        for k in konsonanten:
            for l in vokale:
                for m in zahlen:
                    for n in zahlen:
                        for o in zahlen:
                            for p in zahlen:
                                pswrd = i + j + k + l + m + n + o + p
                                txt.write(pswrd + "\n")
                                txt2.write(pswrd + "\n")
                                counter+= 1
txt2.close()
txt.close
print(counter)
