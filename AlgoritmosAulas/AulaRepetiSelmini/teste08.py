posiInt = int(input("Insira um valor inteiro e positivo: "))

contPrimo= 0
if(posiInt>0):
    for i in range (posiInt):
        if ((posiInt % int(i +1))==0):
            contPrimo = contPrimo + 1
if contPrimo<=2:
        print("O numero é primo")
else:
        print("O numero não é primo")