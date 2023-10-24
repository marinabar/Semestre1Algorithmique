chaine='ab  chsk  apo ab  zbj chs '
alphabet="abcdefghijklmnopqrstuvwxyz"
i=0
mots=''
while i!=len(chaine):
    if chaine[i] in alphabet:
        k=i+1
        mot=chaine[i]
        while chaine[k]!=" ":
            mot+=chaine[k]
            k+=1
        if mot not in chaine[:i]:
            j=i
            index=mot
            f=chaine.find(mot, j)
            print(f'"{mot}"', end=' ')
            while f>=0:
                print(f, end=", ")
                index+=str(f)+" "
                f=chaine.find(mot, f+1)
            mots=mots+mot
            print()
        i=k
    else:
        i+=1