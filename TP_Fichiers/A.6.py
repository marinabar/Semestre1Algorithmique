def lecture(fichier):
    f=open(fichier, "r")
    print(f.read())
    f.close()

lecture('TP7/premier.txt')

def copieFichier(source, destination):
    f1=open(source, "r")
    f2=open(destination, 'w')
    f2.write(f1.read())
    f1.close()
    f2.close()

copieFichier('TP7/premier.txt', "TP7/premiercopie.txt")
    
def copieFichierMiseAJour(source, destination):
    f1=open(source, "r")
    f2=open(destination, 'w')
    txt=f1.read().replace("2021", "2022")
    f2.write(txt)
    f1.close()
    f2.close()

copieFichierMiseAJour('TP7/premier.txt', "TP7/premierCopieMiseAJour.txt")

lecture("TP7/premiercopie.txt")