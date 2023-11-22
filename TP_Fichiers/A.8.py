f=open("TP_Fichiers/nombresDecimaux.txt", "r")
far=open("TP_Fichiers/nombresArrondis.txt", "w")
line=f.readline()
while line:
    nb=float(line.strip("\n"))
    far.write(str(round(nb))+"\n")
    line=f.readline()
f.close()
far.close()
