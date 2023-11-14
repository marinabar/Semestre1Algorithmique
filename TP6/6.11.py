l=[]
t=input('Souhaitez-vous ajouter des nombres à la liste? O ou N ')
while t=="O":
    l.append(input("Quel nombre souhaitez-vous ajouter ? "))
    t=input('Souhaitez-vous ajouter des nombres à la liste? O ou N ')
print(l)