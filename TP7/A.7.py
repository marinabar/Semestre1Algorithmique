f=open("TP7/premier.txt", "r")
fcopie=open("TP7/premiercopietriple.txt", "w")
text=f.read().replace(" ", "   ")
fcopie.write(text)
f.close()
