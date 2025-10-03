import random
Reservas = [0,0,0,0,0,0,0,0,0,0,0,0]
  
for temp in range(len(Reservas)):
        Reservas[temp] = random.randint(0,1)

for temp in range(len(Reservas)):
        print("Assento {}: ".format(temp + 1), end="" )
        if Reservas[temp] == 0:
            print("Vazio")
        else:
            print("Ocupado")
 
Ingres = -1 + int(input("Digite o assento do {}º ingresso: ".format(1)))

for i in range(12): #Verificação
        if Reservas[i] == 0 and (i) == Ingres:
          Reservas[i] == 1
          print("O assento {} foi reservado" .format(i+1))
        
        elif (i) == Ingres:
          print("O assento {} esta ocupado, escolha outro assento" .format(i+1))
          
        else:
          print("O assento {} esta ocupado".format(i+1))
          