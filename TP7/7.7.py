def retirer(L, x):
    for el in L:
        if 0 in L:
            L.remove(0)
    return L

l=[0,1,1,0,2,0]
print(retirer(l, 0))