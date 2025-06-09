a = float(input("insira o valor do numero 1º: "))
b = float(input("insira o valor do numero 2º: "))
c = float(input("insira o valor do numero 3º: "))


if(a==b and a == c ):
    print("Todos os valores são iguais, logo sua diferença é {:.2f}".format(a-c))
if(a>b and a>c):
    if(b>c): aux = a-c
    else: aux= a-b
    print("A subtração entre o maior e o menor numero é {}".format(aux))
elif(b>a and b>c ):
    if(a>c): aux = b-c
    else: aux= b-a
    print("A subtração entre o maior e o menor numero é {}".format(aux))
elif(c>b and c>a):
    if(a>b): aux = c-b
    else: aux= c-a
    print("A subtração entre o maior e o menor numero é {}".format(aux))
elif(a==b and a>c):
    aux= a-c
    print("A subtração entre o maior e o menor numero é {}".format(aux))
elif(a==c and a>b):
    aux= a-b
    print("A subtração entre o maior e o menor numero é {}".format(aux))
elif(c==b and c>a):
    aux= c-a
    print("A subtração entre o maior e o menor numero é {}".format(aux))