selmini = 1000
vetor = []
par=0
impar=0
for i in range(selmini):
    vetor.append(int(input("Insira o {}° valor".format(i+1))))
    
for i in (vetor):
    if(i%2==0):
        par+=1
    else:
        impar+=1

print("Pares: {}\nImpar: {}\nPorcentagem Impar: {:.2f}\nPorcentagem Par: {:.2f}".format(par, impar, impar/selmini,par/selmini))