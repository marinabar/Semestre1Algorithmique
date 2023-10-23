def test2(ch1, ch2='ab'):
    c=ch1.count(ch2)
    if ch1==ch2*c:
        return c
    else:
        return False
print(test2('aaa', 'a'))