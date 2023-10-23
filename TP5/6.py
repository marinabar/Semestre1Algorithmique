ch=input('entrez une chaine à modifier')
v=input("indice val à modifier")
while v!='':
    if int(v)>=len(ch):
        v=input("valeur incorrecte, rentrez indice val à modifier")
    else:
        v=int(v)
        ch=ch[:v]+"?"+ch[v+1:]
        v=input("rentrez indice val à modifier")
print(ch)
