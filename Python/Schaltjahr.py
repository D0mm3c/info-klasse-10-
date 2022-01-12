#-------------------------------------------------------------------------------
# Name:        SchaltjahrTest
# Purpose:     school
#
# Author:      01Dominic.Dietz
#
# Created:     03.11.2021
# Copyright:   (c) 01Dominic.Dietz 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#haendchen weg
def main():
    pass

if __name__ == '__main__':
    main()

#actual code
#input für jahr
jahr=int(input("Gebe dein Jahr ein!"))
#test o teilbar d 4
if(jahr%4==0):
#test o >= 1582
    if(jahr>=1582):
        #test o teilbar d 400 + ausgabe
        if(jahr%400==0):
            print("Das Jahr " + str(jahr) + " ist ein Schaltjahr!")

        else:
            #test o teilbar d 100 +ausgabe
            if(jahr%100==0):
                print("Das Jahr " + str(jahr) + " ist kein Schaltjahr!")

            else:
                print("Das Jahr " + str(jahr) + " ist ein Schaltjahr!")
    else:
        print("Das Jahr " + str(jahr) + " ist ein Schaltjahr!")
else:
    print("Das Jahr " + str(jahr) + " ist kein Schaltjahr!")



