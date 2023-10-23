def test(n, ch2, ch1='habhabab'):
    i=0
    while i <len(ch2):
        if ch2.count(ch2[i])!=1:
            return False
        i+=1
    c=ch1.count(ch2)
    return n==c 

print(test(3, 'ab'))