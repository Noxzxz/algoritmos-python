i = int(input("Quantos produtos sõa comercializados?\n"))
matriz = []
for i in range(i):
    Nome = input("Insira o nome do produto: ")
    Valor = input("Insira o valor do produto: ")
    Estoque = input("Insira a quantidade em estoque")
    matriz.append([Nome, Valor, Estoque])

for temp in range(i): ## maior valor
    if temp == 0: 
        maior = int(matriz[temp][1])
        Nome =  matriz[temp][0]
    elif(maior<int(matriz[temp][1])):
        maior = int(matriz[temp][1])
        Nome =  matriz[temp][0]
print("O produto com o maior valor é {}".format(Nome))
valorT= 0
for temp in range(i+1): ## valor total de cada produto
    valorT += (int(matriz[temp][1]))
    
print("O valor total de cada produto é {}".format(valorT))
valorTOT_EST = 0
for temp in range(i+1): ## valor total de cada produto
    valorTOT_EST += (int(matriz[temp][1])*int(matriz[temp][2]))
    
print("O valor total de produtos em estoque é {}".format(valorTOT_EST))

    
    