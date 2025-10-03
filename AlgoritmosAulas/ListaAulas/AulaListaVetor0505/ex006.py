selmini = 3
vetor = []
primo= []
for i in range(selmini):
    vetor.append(int(input("Insira o {}° valor".format(i+1))))
    
for i in (vetor):
    contP=1
    primas = 0
    while contP<=i:
        if(i%contP==0):
            primas+=1
        contP+=1
    if(primas<=2):
        primo.append(i)

print("Os numeros primos são: ", primo)