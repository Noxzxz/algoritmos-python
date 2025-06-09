i=1
while (i !=0):
    inicio = int(input("Insira o inicio do intervalo: "))
    fim = int(input("insira o fim do intervalo: "))
    perf = []
    contPerf = 0
    contPar = 0 
    if(inicio>=1000 and fim>=1000 and inicio<fim):
        for inicio in range(inicio,fim):
            soma1 = int(inicio/1000) + (int(inicio/100)%10)
            soma2 = ((inicio%100)//10) + (inicio%10)
            if(soma1 == soma2):
                perf.append(inicio)
                contPerf+=1
        for i in range(len(perf)):
            if(perf[i]%2==0):
                contPar+=1
        print("A quantidade de numeros perfeitos no intervalo é {}".format(contPerf))
        print("A Quantidade de numeros perfeitos pares é {} e impares é {}".format(contPar,contPerf-contPar))
    else: 
        print("Dados incorretos tente novamente")
        inicio = int(input("Insira o inicio do intervalo: "))
        fim = int(input("insira o fim do intervalo: "))
    i = int(input("Insira qualquer outro numero alem de 0 para continuar\n"))