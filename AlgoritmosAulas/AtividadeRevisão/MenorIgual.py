a = input("Insira o 1° numero: ")
b = input("Insira o 2° numero: ")
c = input("Insira o 3° numero: ")


if((a==b) or(a==c) or (b==c)):{
    print("Todos os valores devem ser diferentes")}
elif(a<b and a<c):
    print("O menor valor é "+ a)
elif(b<c and b<a):
    print("O menor valor é "+ b)

elif(c<a and c<b):
    print("O menor valor é "+ c)

