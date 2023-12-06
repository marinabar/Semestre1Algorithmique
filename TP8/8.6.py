# Objectif : réalise un mastermind de ligne de commande
import random

def genere(n, b):
    l=[random.randint(1, b) for i in range(n)]
    return l

def enTableau(s):
    return [int(x) for x in s]

def copie(source):
    y=source[:]
    return y

def verification(l1, l2):
    mp=0
    bp=0
    l3=copie(l1)
    l4=copie(l2)
    for i in range(len(l1)):
        if l1[i]==l2[i]:
            bp+=1
            l3.pop(i)
            l4.pop(i)

    for i in range(len(l4)):
        if l4[i] in l3:
            if i!=l3.index(l4[i]):
                mp+=1
                l3.remove(l4[i])
    print("Nombre d'élements bien placés : ", bp)
    print("Nombre d'élements mal placés : ", mp)
    return bp, mp


def mastermind(n, b, nb_essais):
    code=genere(n, b)
    sol=False
    ess=0
    while not sol and ess!=nb_essais:
        nombre=input(f'Saisir un nombre de {n} chiffres (compris entre 1 et {b}) : ')
        nombre=enTableau(nombre)
        bp, mp = verification(code, nombre)
        if bp==n:
            sol=True
            print("Gagné")
        ess+=1
        if ess==nb_essais:
            print('Perdu, dommage la solution était : ', code)
        elif ess==nb_essais-1:
            print("Dernier essai")
        else:
            print(f"Il vous reste {nb_essais - ess} essais")

mastermind(5, 5, 5)