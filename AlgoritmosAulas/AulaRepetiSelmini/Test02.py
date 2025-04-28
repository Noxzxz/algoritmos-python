contador = 1

while contador <= 15:
    a = int(input("Insira o {}° valor: ".format(contador)))
    if(contador == 1):
        aux = a
    elif(aux<a):
        aux = a
    contador =  contador + 1

print("O maior valor informado é {}".format(aux))