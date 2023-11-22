def lectureFichier(nom):
    f=open(nom, "r")
    l=f.readlines()
    f.close()
    return l

def ecritureFichier(nom, liste):
    f=open(nom, 'w')
    for el in liste:
        f.write(el+"\n")
    f.close()

def triFichier():
    lignes=lectureFichier("TP_Fichiers/notesGr1.txt")
    lignes.sort()
    ecritureFichier("TP_Fichiers/notesGr1_trie.txt", lignes)

def triFichier(N):
    for i in range(1, N+1):  
        lignes=lectureFichier(f"TP_Fichiers/notesGr{i}.txt")
        lignes.sort()
        ecritureFichier(f"TP_Fichiers/notesGr{i}_trie.txt", lignes)

triFichier()