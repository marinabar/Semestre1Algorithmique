def filtrage(Lr):
    Lrfil=Lr.copy()
    i=0
    while i<len(Lrfil):
        if Lrfil[i]<0:
            Lrfil.pop(i)
        i=i+1
    return Lrfil

L=[1, 4, -5, 8, -8, 1]
print("Liste après filtrage : " , filtrage(L))
print("Liste avant filtrage", L)