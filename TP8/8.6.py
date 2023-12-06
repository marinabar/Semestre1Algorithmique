# Objectif : réalise un mastermind de ligne de commande
import random

def genere(n, b):
    l=[random.randint(1, b) for i in range(n)]
    return l

def enTableau(s):
    return list(s)

def copie(source):
    y=source[:]
    print(id(y), id(source))
    return y

print(enTableau("2432"))

def verification(l1, l2):
    mp=0
    bp=0
    for i in range(len(l1)):
        if l1[i]==l2[i]:
            bp+=1
        elif l2[i] in l1:
            mp+=1
    return bp, mp
print(verification([1, 3, 2, 5], [3, 3, 2, 9]))