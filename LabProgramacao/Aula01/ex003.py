def contagem(a,b):
    c=0
    for i in range(a,b):
        c+=1
    return print(c)

a = int(input("Insira o 1° numero: "))
b = int(input("Insira o 2° numero: "))
contagem(a,b)