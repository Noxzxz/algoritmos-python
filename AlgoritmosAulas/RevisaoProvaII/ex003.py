import ex001_util;
a = int(input("Insira o numero de espaços no vetor: "))
vetor = [0]*a

for i in range(0,a):
    vetor[i] = int(input("Insira o {}º valor: ".format(i+1)))

vetor = ex001_util.ordenar(vetor,1)
print("Os maiores valores são {}, {}, {}".format(vetor[0],vetor[1],vetor[2]))
