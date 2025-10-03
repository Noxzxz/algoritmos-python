rows = int(input("Insira o numedo de linhas da matriz: "))
collum = int(input("Insira o numedo de colunas da matriz: "))

m = [[int(input("Valor: ")) for j in range(collum)] for i in range(rows)]

print(m)