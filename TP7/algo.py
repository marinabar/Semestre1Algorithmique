
def harshad(n):
    return n%sum(list(map(int, str(n).strip())))==0

print(harshad(113))


x1=100
x2=120

i=x1
prem=0
n=0

while i <=x2:
    if harshad(i) and n!=0:
        n+=1
    elif harshad(i):
        n=1
        prem=i
    else:
        n=0
        prem=0
    i+=1

k=0
while k!=n:
    print(prem+k)
    k+=1