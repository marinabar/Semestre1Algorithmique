f=open("TP7/multiplication.txt", "w")
for i in range(2, 31):
    for j in range(1, 21):
        t=f'{str(i)} x {str(j)} = {str(i*j)} \n'
        print(t)
        f.write(t)
    f.write('\n')
f.close()