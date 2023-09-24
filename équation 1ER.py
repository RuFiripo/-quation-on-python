# -*- CODING MARK: 13 -*-
#
# APPRENDRE À FAIRE DES ÉQUATIONS EN PYTHON
#
# aide et enseignements de : VICTOR HUGO
#                            EMAIL: VICTORHGDASILVA2017@OUTLOOK.COM
# 
# -----------------------------------------

import math 
import time 

print("\t POUR CONTINUER, CHOISISSEZ L'UNE DES OPTIONS SUIVANTES : \n")

a = input("ÉQUATIONS DU 1ER DEGRÉ ----> \n'1'\n"
          "ARRÊTER ----> \n'EXIT'\n")


if a == 'exit':
    print("\t CHARGEMENT....\n")

    loop = 0
    time.sleep(1.2) 

    exit()

elif a == '1':
    print("\t CHARGEMENT....\n") 

    loop = 0
    time.sleep(1.2)

    print("\t ÉQUATIONS DU 1ER DEGRÉ: \n")

    ax = input("ENTREZ LA VALEUR DE A: ")
    b = input("ENTREZ LA VALEUR DE B: ")
    c = input("ENTREZ LA VALEUR DE C: ")

    resp = (float(b) - float(c)) / float(ax) #FORMULE

    if resp == '0':
        print("\t CHARGEMENT....\n")

        loop = 0
        time.sleep(1.3)

        print("\t LA VALEUR DE X EST NULLE (0) \n")


    else:
        print("\t CHARGEMENT....\n")

        loop = 0
        time.sleep(1.3)

        print("\t LA VALEUR DE X EST:",resp," \n")  