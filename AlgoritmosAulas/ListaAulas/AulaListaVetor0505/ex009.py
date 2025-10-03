i = int(input("Quantos produtos sõa comercializados?\n"))
matriz = []
for i in range(i):
    Nome = input("Insira o nome do produto: ")
    Valor = input("Insira o valor do produto ano passo: ")
    atual = input("Insira o valor do produto atualmente: ")
    matriz.append([Nome, Valor, atual])
    

for temp in range(i+1): ## valor total de cada produto
    Porcetagen = (int(matriz[temp][2])/int(matriz[temp][1]))
    print("A porcentagem de aumento do produto {} é: {:.0f}%".format(matriz[temp][0],Porcetagen*100))

    
    