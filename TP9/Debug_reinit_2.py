from random import randint

def f(n):
    L = []
    for i in range(n):
        L.append(randint(0,10))
    return L

M = f(5)
print(M)


# L'erreur L is not defined est apparue dès le début dans mon cas