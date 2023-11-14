import random

def TabAlea(n, a, b):
    l=[]
    for i in range(n):
        l.append(random.randint(a, b))
    return l


def TabProduit(T):
    p=1
    for i in T:
        p*=i
    return p


n=int(input("entrez n : "))
a=int(input("entrez a : "))
b=int(input("entrez b : "))

t=TabAlea(n, a, b)
print(t)
print(TabProduit(t))