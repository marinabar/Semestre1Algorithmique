"""from 7.9 import listAlea"""
import time


from random import randint
def listAlea(n, a, b):
    l=[]
    for i in range(n):
        l.append(randint(a, b))
    return l



# algorithme naif
def somme(l):
    return sum(l)

def coupemin1(s):
    deb=time.time()
    mini=s[0]
    val=(0)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if somme(s[i:j])<mini:
                mini=somme(s[i:j])
                val=(i, j-1)
    fin=time.time()
    print("Temps d'exécution : ", fin-deb)
    return mini, val


def coupei(s):

    mini=s[0]
    for i in range(1, len(s)):
        if mini + s[i]>mini:
            return mini
        else:
            mini=mini + s[i]

    return mini

def coupemin2(s):
    deb=time.time()
    mini=s[0]
    for i in range(len(s)):
        l=coupei(s[i:])
        if l<mini:
            mini=l
    
    fin=time.time()
    print("Temps d'exécution : ", fin-deb)
    return mini


def coupemin3(s):
    deb=time.time()
    v=s[0]
    m=v
    for i in range(len(s)):
        m=min(m +s[i], s[i])
        v=min(v, m)
    
    
    fin=time.time()
    print("Temps d'exécution : ", fin-deb)

    return v

s1=listAlea(100, -100, 100)
print("temps pour la liste 1")
coupemin1(s1)
coupemin2(s1)
coupemin2(s1)
s2=listAlea(600, -100, 100)
print("temps pour la liste 2")
coupemin1(s2)
coupemin2(s2)
coupemin2(s2)
s3=listAlea(1100, -100, 100)
print("temps pour la liste 3")
coupemin1(s3)
coupemin2(s3)
coupemin2(s3)
s4=listAlea(1600, -100, 100)
print("temps pour la liste 4")
coupemin1(s4)
coupemin2(s4)
coupemin2(s4)

# Dernier algorithme le plus rapide, mais différence moindre en le 2 et le 3 par rapport à l'écart avec le 1