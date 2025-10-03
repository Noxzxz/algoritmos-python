def GerarMatriz():
    ordem = 5
    matriz = [[randint(0,10) for j in range(ordem)]for i in range (ordem)]
    return matriz

def imprimir(m):
    for i in range(len(m)):
        for j in range (len(m)):
            print(m[i][j],end="\t")
        print("\n")
    
def criptografar(a):    
    contador = 0
    for i in range(len(a)):
        for j in range (len(a)):
            if((i+j) == (len(a)-1)):
                aux = a[contador][contador]
                a[contador][contador] = a[i][j]
                a[i][j] = aux
                contador+=1
    return a
    
#Codigo Bruto
from random import randint

m = GerarMatriz()
imprimir(m)
m = criptografar(m)
print("Revelação")
imprimir(m)

