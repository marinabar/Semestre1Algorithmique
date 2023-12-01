def reverse(chaine):
    lmots = []
    mot = ""
    
    for char in chaine:
        if char == " ":
            lmots.append(" " + mot)
            mot = ""
        else:
            mot+= char
    lmots.append(mot)
    lmots=lmots[::-1]
    reverse=""
    for mot in lmots:
       reverse += mot
    return reverse
print(reverse("Ceci est une chaine python"))

def optimrev(chaine):
    return " ".join(chaine.split()[::-1])
print(optimrev("Ceci est une chaine python"))