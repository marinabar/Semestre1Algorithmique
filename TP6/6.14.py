def lireDistance():
    l=[[]]*5
    for i in range(5):
        l[i]=[0]*5
        for j in range(5):
            if j<i:
                l[i][j]=l[j][i]
            elif j==i:
                l[i][j]=0   
            else:
                d=int(input(f"Entrez la distance de la ville {i} à {j} "))
                l[i][j]=d
    return l
d=lireDistance()
print(d)
villes=["Auxerre", "Avallon", "Clamecy", "Joigny", "Migennes"]

def inegalitetri(d):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if d[i][j]> d[i][k]+ d[k][j]:
                    print(i, j, k)
                    print(f"Villes concernées : , {villes[i]}, {villes[j]}, {villes[k]}")

inegalitetri(d)



