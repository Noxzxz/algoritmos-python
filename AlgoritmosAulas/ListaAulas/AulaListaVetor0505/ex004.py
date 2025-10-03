Selmini = 1000
vetor = []
maior = 0
menor = 0 
for i in range(Selmini):
    vetor.append(input("Insira um valor"))

for i in (vetor):
    if(i == vetor[1]):
        maior=int(i)
        menor=int(i)
        
    elif(maior<int(i)):
        maior=int(i)
    elif(menor>int(i)):
        menor = int(i)

print("Os valores inseridos são: ", vetor)
print("O menor valor é {}\nO maior valor é {}".format(menor, maior))