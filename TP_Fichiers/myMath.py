def fact(n):
    m=1
    for i in range(1, n+1):
        m=m*i
    return m

def binome(n, p):
    return round(fact(n)/(fact(p)*fact(n-p)))

def triangle(n):
    for i in range(n+1):
        print(binome(n, i), end=" ")    


# vérifie que le code soit lu en tant que fichier principal
if __name__=="__main__":
    print(binome(5, 3))