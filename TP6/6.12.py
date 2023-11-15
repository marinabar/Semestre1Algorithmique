l=[[1, 2, 3], [], [2, 3, 0, 4]]
maxi=[]
for liste in l:
    if len(liste)>len(maxi):
        maxi=liste

s=0
for el in maxi:
    s+=el
print(s)