numCont = int(input("insira o numero da conta: "))
vet1 = numCont%10
vet2 = (numCont//10)%10
vet3 = ((numCont//10)//10)%10

SomaNum = (vet3 + vet2*10 + vet1*100) + numCont

print(vet1,vet2,vet3,SomaNum)

vet1 = SomaNum%10
vet2 = (SomaNum//10)%10
vet3 = ((SomaNum//10)//10)%10 

MultNum = (vet1*1)+(vet2*2)+(vet3*3)

print(vet1,vet2,vet3, MultNum)

print("O digitor verificador é {}".format(MultNum%10))