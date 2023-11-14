l=[]
n=int(input('entrez n '))
p=int(input('entrez p '))
for i in range(1,n+1):
    l.append(i*7)
    print(l[-1], end="; ")
    if i%p==0:
        print()
print("Vous avez affiché ", n//p, " multiples de ", p)