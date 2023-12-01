from random import randint
def listAlea(n, a, b):
    l=[]
    for i in range(n):
        l.append(randint(a, b))
    return l
def absences(l):
    s=0
    for i in range(100):
        if i not in l: 
            s+=1
    return s


somme=sum([absences(listAlea(100, 0, 99)) for i in range(1000)])
print(somme/1000)
# ~~ 36 : valeur étonnante