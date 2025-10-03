selmini = 3
vetor = []
vetorInv = []
for i in range (selmini):
    vetor.append(int(input("Insira o Valor {}°: ".format(i+1))))

print(vetor)
vetor.reverse()
print(vetor)

while selmini>0:
    vetorInv.append(vetor[selmini-1])
    selmini-=1
    
print(vetorInv)

for i in range(3,1):
    vetor.append(vetorInv[i])
    
print(vetor)