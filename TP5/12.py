import random
def permutemot(mot):
    p=mot[0]
    d=mot[-1]
    i=1
    if len(mot)<=3:
        return mot
    while i!=len(mot)-2:
        index=random.randint(i+1, len(mot) - 2)
        mot = mot[0:i] + mot[index] + mot[i+1:index] + mot[i] + mot[index+1:]
        i+=1
    return mot

def permutephrase(phrase):
    assert phrase!='', "merci de donner une entrée textuelle"
    phrase=" "+phrase+" "
    i=0
    k=0
    nbmots=phrase.count(' ')-1
    while k !=nbmots:
        j=phrase.find(' ', i+1)
        phrase=phrase[:i+1]+permutemot(phrase[i+1:j])+phrase[j:]
        print(phrase)
        i=j
        k+=1
    return phrase.strip()

phrase=input("entrez une phrase à permuter ")
print(permutephrase(phrase))