
def split(word):
    return [char for char in word]

usernamelist = ["der8ecker","faloreceb"]
passwordlist = []
sonderzeichen = ["!","#","?","+","'",";",":","^","§","$","%","&","/","(",")","="]
zahlen = ["0","1","2","3","4","5","6","7","8","9"]

while True:
    loginorregister = input("Wollen Sie sich anmelden oder neu registrieren? geben sie l ein, um sich einzuloggen und r, um sich zu registrieren. : ")
    loginorregister = str(loginorregister).lower()

    if(loginorregister=="r"):
        print("Registrierung wird nun durchgeführt.")
        while True:
            username = input("Welchen Nutzernamen möchten Sie haben?: ")
            username = str(username)
            index = 0
            inlistuser = (username in usernamelist)
            if(inlistuser==True):
                print("Der Nutzername ist leider bereits vergeben.")
                print("Bitte versuchen Sie es erneut.")
                break
            if(inlistuser==False):
                while True:
                    print("Bitte geben Sie nun Ihr Passwort ein, welches Sie gerne hätten.")
                    print("Das Passwort muss mindestens 8 Zeichen lang sein und mindestens eine Zahl und Sonderzeichen beinhalten. ")
                    password = input("Mein gewünschtes Passwort lautet: ")
                    index = 0
                    while(index<len(password)):
                        passwordlist.append(password[index])
                        index+=1

                    while(index<len(password)):
                        global sonderzeichentrue
                        sonderzeichentrue = password[index] in sonderzeichen
                        if(sonderzeichentrue == "True"):
                            #global sonderzeichentrue
                            print("Sonderzeichen ist enthalten")
                        index+=1
                    while(index < len(password)):
                        global zahlentrue
                        zahlentrue = password[index] in zahlen
                        if (zahlentrue == "True"):
                            #global zahlentrue
                            print("Eine Zahl ist enthalten")
                        index += 1
                    if(len(password)>7):
                        if(sonderzeichentrue == "True"):
                            if(zahlentrue == "True"):
#danke jonas das war der brüller