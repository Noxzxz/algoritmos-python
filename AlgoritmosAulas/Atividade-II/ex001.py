a = int(input("Insira o primeiro numero do intervalo: "))
b = int(input("O numero final intervalo: "))

matrizPerfeito=[]

for i in range (a,b):
    div = 0
    for c in range (1,i):
        if(i%c==0):
                div+= c
    if(i == div):{
        matrizPerfeito.append(div)
    }
        
print("Os numeros perfeitos são ", matrizPerfeito)