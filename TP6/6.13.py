notes=[2, 12, 0, 0, 8, 7, 20, 11,20, 0, 12]
etu=["Florian", 'Antoine', "Charles1", "Robert", "Charles2", "Erwan", "Jean", "Xavier", "Didier", "Alain", "Hadi"]

while input("souhaitez vous ajouter de nouvelles valeurs ? O ou N")=="O":
    notes.append(int(input("Saisir une note ")))
    etu.append(int(input("Saisir un nom ")))

i=0
while i!=len(notes):
    if notes[i]==0:
        notes.pop(i)
        etu.pop(i)
        i-=1
    i+=1

print(f"moyenne des notes de l'examen : {round(sum(notes)/len(notes), 2)}")

admis=[]
recal=[]
for i in range(len(notes)):

    if notes[i]>=10:
        print(f'{etu[i]} a obtenu {notes[i]} et est admis')
        admis.append(etu[i])
    else:
        print(f'{etu[i]} a obtenu {notes[i]} et est recalé')
        recal.append(etu[i])
