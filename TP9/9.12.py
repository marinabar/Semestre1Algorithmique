def sommeRec(n):
    if n==0:
        return 0
    else:
        return n + sommeRec(n-1)
    
def sommeRec2(debut, fin):
    if debut==fin:
        return 0
    else:
        return debut + sommeRec2(debut+1, fin)
print(sommeRec(10))
print(sommeRec2(50, 60))