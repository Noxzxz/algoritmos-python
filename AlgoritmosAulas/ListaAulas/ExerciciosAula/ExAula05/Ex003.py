x1 = int(input("Insira o valor do x da coordenada 1: "))
y1 = int(input("Insira o valor do y da coordenada 1: "))

x2 = int(input("Insira o valor do x da coordenada 1: "))
y2 = int(input("Insira o valor do y da coordenada 1: "))

CalcLoc1= ((x1)**2 + (y1)**2)**1/2
CalcLoc2= ((x2)**2 + (y2)**2)**1/2

print("As respectivas coordenadas {},{} e {},{}".format(x1,y1,x2,y2))
if(CalcLoc1<CalcLoc2):
    print("A coordenada 1 é a mais proxima da origem")
elif(CalcLoc2==CalcLoc1):
    print("Ambas as coordenadas tem a mesma distancia da origem")
else:
    print("A coordenada 2 é a mais proxima da origem")