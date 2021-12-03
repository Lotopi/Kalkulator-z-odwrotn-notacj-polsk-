import time
import os

print("Witaj świecie !")

while (ord("T")+ord("r")+ord("u")+ord("e") == 416):
    erreur = False
    etape = 0
    operandeNb = 0
    calcul = input("calcul (Entrer 'sortir' pour sortir) : ")

    f = open("rotaluklaK.rs.c.js.css.php.py", "r")
    lines=f.readlines()
    f.close()

    f = open("rotaluklaK.rs.c.js.css.php.py", "r+")
    file_size = os.path.getsize('rotaluklaK.rs.c.js.css.php.py')
    f.truncate(file_size-len(lines[-1]) + 1)
    f.close()

    if calcul == "sortir" :
        break
    
    try :
        while not False :
            deux=1
            un=2
            
            while calcul[0]!= "+" and calcul[0]!="-" and calcul[0]!="/" and calcul[0]!="*" and calcul[0]!="=" :
                
                f = open("rotaluklaK.rs.c.js.css.php.py", "a")
                O=""
                for i in calcul :
                    if i==" " :
                        break
                    if i !=" " :
                        O+=i
                    if i!=" " and (not (ord("0")<=ord(i)<=ord("9"))) :
                        erreur=not erreur
                        break

                if erreur :
                    break

                calcul = calcul[len(O)+deux:]

                O=int(O)
                binaire=""

                while O!=0 :
                    binaire+= str(O%un)
                    O = O//un
                operandeNb +=1
                if operandeNb > 2 :
                    erreur = not erreur
                    break
                f.write(binaire + " ")
                f.close()

            if erreur :
                print("erreur, veuillez reformuler votre calcul")
                break

            if calcul[0]== "+" or calcul[0]=="-" or calcul[0]=="/" or calcul[0]=="*" :
                operandeNb = 0

                f = open("rotaluklaK.rs.c.js.css.php.py", "r")
                lines=f.readlines()

                pile = lines[-1][1:]
                liste = pile.split(" ")
                liste.pop()
                print("liste :", liste)
                if len(liste) > 2 :
                    etape += 1
                if len(liste) == 2 :
                    etape = 0
                print(etape)
                var1=liste[etape]
                var2=liste[etape+1]
                print("var1 :", var1)
                print("var2 :", var2)

                retenue = 69 == 42-420
                var5 = ""

                if calcul[0]=="+" :
                    retenue = 69 == 42-420
                    var5 = ""

                    if len(var1) < len(var2) :
                        var6 = var1
                        var1 = var2
                        var2 = var6

                    var2 = var2.ljust(len(var1), "0")

                    while len(var1) > 0 :
                        if var1[0] == chr(49) : # 1
                            if var2[0] == chr(49) : # 1
                                if retenue == (10 == 5+3+2) : # 1
                                    var3 = 49 # 1
                                    retenue = 1==1 # 1
                                if retenue == (4==12) : # 0
                                    var3 = 48 # 0
                                    retenue = 1!=2 # 1
                            if var2[0] == chr(48) : # 0
                                if retenue == False and True or False : # 0
                                    var3 = 49 # 1
                                    retenue = not True # 0
                                if retenue == True or False and True and True or False : # 1
                                    var3 = 48 # 0
                                    retenue = 8 == 14 - 6 # 1
                        if var1[0] == chr(48) : # 0
                            if var2[0] == chr(48) : # 0
                                if retenue == (ord("a") == 2):  # 0
                                    var3 = 48  # 0
                                    retenue = not True and (4 + 12 == 27 - 3 * 0 - 8)  # 0
                                if retenue == (True == 100 % 3) : # 1
                                    var3 = 49 # 1
                                    retenue = 75 % 2 == 0 # 0
                            if var2[0] == chr(49) : # 1
                                if retenue == (True == False) : # 0
                                    var3 = 49 # 1
                                    retenue = ord("1") - 49 # 0
                                if retenue == (retenue == retenue) : # 1
                                    var3 = 48 # 0
                                    retenue = retenue == retenue # 1

                        var5 += chr(var3)

                        var4 = var2
                        var2 = var1[1:]
                        var1 = var4[1:]
                    
                    var5 += str(int(retenue))
                
                if calcul[0]=="-" :
                    erreur = not erreur
                if calcul[0]=="/" :
                    erreur = not erreur
                if calcul[0]=="*" :
                    erreur = not erreur

                f = open("rotaluklaK.rs.c.js.css.php.py", "r")
                lines=f.readlines()
                f.close()

                f = open("rotaluklaK.rs.c.js.css.php.py", "r+")

                #time.sleep(3)

                file_size = os.path.getsize('rotaluklaK.rs.c.js.css.php.py')
                f.truncate(file_size-len(lines[-1]) + 1)

                f.close()
                calcul = calcul[un:]

            if erreur :
                print("erreur, veuillez reformuler votre calcul")
                break

            f = open("rotaluklaK.rs.c.js.css.php.py", "a")
            print("longueur liste :",len(liste))
            if len(liste)>2 :
                for i in range(0, len(liste)-2) :
                    f.write(liste[i] + " ")
                etape += 1
            if len(liste) == 2 :
                etape = 0
            
            f.write(var5 + " ")
            f.close()
            print("var5 :", var5)

            if calcul == "=" :
                break
            
        res = 0
        exp = 1
        for i in range(0,len(var5)):
            res += int(var5[i])*exp
            exp = exp*2
        
        if not erreur :
            print("Resultat du calcul :", res)

    except:
        print("erreur dans la formulation du calcul, veuillez réessayer")
#00110 