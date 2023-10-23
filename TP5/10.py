chaine=input('mot à transformer ')
n= len(chaine)

for i in range(n):
    for j in range(n):
        if j == i or j == n - 1 - i:
            print(chaine[j], end=' ')
        else:
            print(' ', end=' ')
    print("\n")

