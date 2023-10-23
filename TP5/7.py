chaine=input("rentrez une chaine de caractères ")
i=1
comp=0
n=len(chaine)
while i<len(chaine):
    if chaine[i]==chaine[i-1]:
        chaine=chaine[:i-1]+chaine[i:]
        i-=1
    i+=1
print(chaine)