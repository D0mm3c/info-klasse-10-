#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      01Philip.Rohde
#
# Created:     05.01.2022
# Copyright:   (c) 01Philip.Rohde 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Zufallsgenerator randint importieren
from random import randint

def main():
    pass

if __name__ == '__main__':
    main()

#Wertzuweisungen der Zufahlszahl, der Versuche und der Ratezahl
zz = randint(1,1000)
vz = 0
rz = 0

#anzeigen der zu erratenden Zahl
print(int(zz))

#Schleife die sich wiederholt wenn man weniger als 10 Versuche hat und noch nicht erraten
while((vz<10) and (zz!=rz)):
#Eingabe der Zahl die man errÃ¤t
    rz = int(input("Gib deine Ratezahl ein!"))
    vz+=1
#Test ob die Ratezahl der Zufallszahl entspricht
    if(rz==zz):
#Antworten fÃ¼r verschieden viele Versuche
        print("Du hast es richtig erraten!" + "Du hast die Zahl " + str(zz) + " in " + str(vz) + " Versuchen erraten!")
        if(vz==1):
            print("Du hattest wohl viel GlÃ¼ck!")
        if(vz==2 or vz==3 or vz==4):
            print("Du hast es gut gemacht!")
        if(vz==5 or vz==6 or vz==7):
            print("Du hast es geschafft aber es hÃ¤tte besser sein kÃ¶nnen!")
        if(vz==8 or vz==9 or vz==10):
            print("Du hast es gerade noch so geschafft!")
#prÃ¼fen ob Ratezahl grÃ¶ÃŸer als Zufallszahl und dann antwort ob grÃ¶ÃŸer oder kleiner sein muss
    else:
        if(rz>zz):
            print("Du hast zu groÃŸ geraten!")

        else:
            print("Du hast zu klein geraten!")
#wenn Versuche 10 sind hat man verloren
    if(vz>10):
        print("Du warst zu schlecht!")

