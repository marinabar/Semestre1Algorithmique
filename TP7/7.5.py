n = int(input("Combien de multiples de 7 à afficher ? "))
p = int(input("Aller à la ligne après chaque multiple de combien ? "))
multi=[]
for i in range(1, n):
    multi.append(7*i)
nb = 0
for i in range(n-1):
    if (i+1)%p == 0:
        print(multi[i])
        nb+=1
    else:
        print(multi[i], end=" ; ")
print("\nVous avez affiché", nb, "multiples de", p)
