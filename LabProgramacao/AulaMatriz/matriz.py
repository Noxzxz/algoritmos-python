rows = int(input("Insira o numedo de linhas da matriz: "))
collum = int(input("Insira o numedo de colunas da matriz: "))

y,x   =  [],[]
for j in range (rows):
    x=[]
    for i in range (collum):
        x.append(i)
    y.append(x)
    
print(y)