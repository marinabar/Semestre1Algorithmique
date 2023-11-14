somme=0

n=int(input("entrez un entier : "))

for i in range(1,n+1):
    somme+=i
print(somme)
# version avec sum
print(sum(range(1, n+1)))