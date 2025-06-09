a = int(input("Insira um numero: "))

matrizPrimo= []
T=1
for i in range(2,a+1):
    if(a%i==0):
        div= 0
        for T in range(1,i):
            if(i%T==0):
                div+= 1
        if(div<2):
            matrizPrimo.append(i)

maior = matrizPrimo[0]
for i in (matrizPrimo):
    if(maior<i):
        maior=i

print("O numero {} tem {} como divisores primos, o maior fator primo é {}".format(a, matrizPrimo,maior))