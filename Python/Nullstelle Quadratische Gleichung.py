#-------------------------------------------------------------------------------
# Name:        Nullstellenberechnung einer quadratischen Gleichung
# Purpose:
#
# Author:      01Dominic.Dietz
#
# Created:     24.11.2021
# Copyright:   (c) 01Dominic.Dietz 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#haendchen weg
def main():
    pass

if __name__ == '__main__':
    main()

#programm bidde
#wurzel wird von mathe importiert
from math import sqrt


nochmal="y"
while(nochmal=="y"):
#eingabe der werte
    print("Es wird ein quadratische Gleichung mit der Form 'ax^2+bx+c' berechnet!")
    a=float(input("Gib a der quadratischen Gleichung ein!"))
    b=float(input("Gib b der quadratischen Gleichung ein!"))
    c=float(input("Gib c der quadratischen Gleichung ein!"))
#pruefen ob a,b oder c null ist
    if(a == 0):
        if(b == 0):
            if(c == 0):
                LM="L=R"

            else:
                LM="L={}"
#wenn a 0 wird hier trotzdem eine loesung ermittelt fuer eine lineare funktion
        else:
            x1= round(-b/c,3)
            LM="L={" + str(x1) + "}"
#wenn c 0 ist wird hier die eine nullstelle berechnet
    else:
        if((b/(2*a))**2 == c/a ):
            x1= round(-b/(2*a), 3)
            LM="L{" + str(x1) + "}"

#wenn c groesser 0 wird hier ausgegeben dass es keine loesung gibt
        else:
            if(c/a > (b/(2*a))**2 ):
                LM="L={}"
#wenn es eine normale quadratische gleichung werden hier beide werte berechent
            else:
                x1 = round(-b/2*a + sqrt((b/2*a)**2 - c/a), 3)
                x2 = round(-b/2*a - sqrt((b/2*a)**2 - c/a), 3)
                LM = "L{" + str(x1) + "; " + str(x2) + "}"


    print(LM)
#hier wird gefragt ob das Programm wiederholt werden soll

    nochmal=str(input("Nochmal? y fuer yes oder andere Taste zum beenden"))
    nochmal=nochmal.lower()
    print(nochmal)





print("Ende")







