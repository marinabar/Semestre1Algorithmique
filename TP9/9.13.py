def fiborec(n):
    if n==1 or n==2:
        return 1
    else:
        return fiborec(n-1)+fiborec(n-2)
    
print(fiborec(6))

def fiboit(n):
    s=0
    a=1
    b=1
    for i in range(n-2):
        s=a+b
        a, b=b, s
    return s
print(fiboit(6))