f=open("TP7/nombresDecimaux.txt", "r")
far=open("TP7/nombresArrondis.txt", "w")
line=f.readline()
while line:
    nb=float(line.strip("\n"))
    far.write(str(round(nb))+"\n")
    line=f.readline()
f.close()
far.close()
