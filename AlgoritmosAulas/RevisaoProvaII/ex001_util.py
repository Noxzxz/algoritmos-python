
def calcular_maior(a):
    maior = a[0]
    for i in range(1,len(a)):
        if(maior<int(a[i])):
            maior = int(a[i])
    return maior

def calcular_menor(a):
    menor = a[0]
    for i in range(1,len(a)):
        if menor>int(a[i]):
            menor = int(a[i])
    return menor

def calcular_media(a):
    media = 0
    for i in range(0,len(a)):
         media += a[i]
    media = media/len(a)
    return media

def binario(a):
    a = int(a)
    bin = ""
    while a>0:
        resto = a%2
        bin = str(resto) + bin
        a = a//2
    return(bin)

def binario2(a):
    a = int(a)
    bin,i = 0,0
    if(a==0):
        return a
    while a>0:
        calc = a%2
        bin += calc*(10**(i))
        i+=1
        a= a//2
    return bin

def hex(a):
    a = int(a)
    hexa = ''
    digitHexa = '0123456789ABCDEF'
    if(a==0):
        print(0)
    while(a>0):
        calc = a%16
        hexa= digitHexa[calc] + hexa
        a = a//16
    return hexa

def ordenar(a,b):
    if(b==0):
        for j in range(1,len(a)):
            for i in range(0,len(a)-1):
                if(a[i]>a[i+1]):
                    aux = a[i]
                    a[i] = a[i+1]
                    a[i+1] = aux
    if(b==1):
        for j in range(1,len(a)):
            for i in range(0,len(a)-1):
                if(a[i]<a[i+1]):
                    aux = a[i]
                    a[i] = a[i+1]
                    a[i+1] = aux
    return a

a = [10,9,8,21,7]
"""teste a
print(calcular_maior(a))
print(calcular_menor(a))
print(calcular_media(a))
print(binario(10))
print(binario2(10))
print(hex(687))
print(ordenar(a,0))
print(ordenar(a,1))"""


