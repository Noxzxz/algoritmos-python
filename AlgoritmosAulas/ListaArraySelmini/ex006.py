atlet = int(input("Insira o numero de atletas: "))

nomes = []
dist1 = []
dist2 = []
for i in range(atlet):
    nomes.append(input("Insira o nome do atleta {}º".format(i+1)))
    dist1.append(int(input("Insira a distancia do 1º disparo: ")))
    dist2.append(int(input("Insira a distancia do 2º disparo: ")))

for i in range(atlet):
    if(i==0):
        menor= ((dist1[i]+dist2[i])/2)
    if(menor>((dist1[i]+dist2[i])/2)):
        menor = ((dist1[i]+dist2[i])/2)
        
for i in range(atlet):
    if((dist1[i]+dist2[i])/2== menor):
        print("O competido que venceu a competição foi: ",nomes[i])