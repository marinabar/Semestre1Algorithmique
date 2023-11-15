f=open("TP7/Testmako.txt", 'r')
allr=f.read()
print(allr)

f.seek(0)
lines=f.readlines()
print(lines)
for line in lines:
    print(line.strip('\n'))

f.seek(0)
l=[]
for line in f:
    l.append(line)
print(l)
f.close()

for line in l:
    print(line.strip("\n"))
