def permute(mot1, mot2):
    i=0
    x=0
    while i!=(len(mot2)):
        if mot1.find(mot2[i])<x:
            return "impossible"
        else:
            x=mot1.find(mot2[i])
        i+=1
    return "OK"
print(permute('abcde', "xa"))