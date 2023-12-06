# questions 1 et 2
def echange(a, b):
    a, b=b, a
    return a, b

a=3
b=4
a, b = echange(a, b)

print("a = ", a)
print("b = ", b)

#question 2

def echangeliste(L):
    L[0], L[1]=L[1], L[0]
    return L

print(echangeliste([4, 2]))

#question 3
def echangeAB():
    global a 
    global b 
    tmp=a
    a=b
    b=tmp

a=2
b=3
echangeAB()
print("a = ", a)
print("b = ", b)