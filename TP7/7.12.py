import random

E=['Luc', 'Martin', 'Gaulois', 'Johan', 'Jonathan']
S=[3, 2, 4]
def salle(E, c):
    if c>len(E):
        return E
    return random.sample(E, c)

def affectation(E, S):
    l=[]
    totals=sum(S)
    totale=len(E)
    vides=(totals-totale)//len(S)

    print(vides)
    for el in S:
        lsalle=salle(E, el - vides)

        l.append(lsalle)
        E=[e for e in E if e not in lsalle]
    return l 

def emargement(l):
    for i in range(len(l)):
        f=open(f"emargement_{i}.txt", "w")
        f.write("Feuille d'émargement\n")
        for nom in l[i]:
            f.write(nom + "\n")
        f.write(str(len(l[i])))
        f.close()


f=open("TP7/L1.txt", "r")
E=f.readlines()
f.close()
E = [s.strip() for s in E]
s=4
LS=[]
LS=[40, 20, 30, 40, 100]
"""for i in range(s):
    LS.append(int(input("Quelle est la capacité de cette salle ? ")))"""

emargement(affectation(E, LS))