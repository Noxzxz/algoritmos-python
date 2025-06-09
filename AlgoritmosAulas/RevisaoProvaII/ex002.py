import ex001_util;

n = int(input("insira o tamanho do vetor: "))
vetor = [0]*n
for i in range(0,n):
    vetor[i] = int(input("Insira o {}º numero: ".format(i)))

print(vetor)
print("O maior valor é {}, o menor valor é {}".format(ex001_util.calcular_maior(vetor),ex001_util.calcular_menor(vetor)))