import SomaMDL
a = int(input("Insira o valor das variaveis A e B: "))
b = float(input())

i=0
while i < 1:
    c = int(input("Escolha entre os numeros 1 à 4 para escolher a operação matematica\n1 - soma   2 - subtração   3 - multiplicação   4 - Divisão\n "))
    if c == 1:
        resultado = SomaMDL.soma(a,b)
        print("O resultado da soma é {}".format(resultado))
        esc = int(input("Para finalizar o script digite 1, para continuar com as operações digite 2 "))
        if esc == 1:
                i = i+1
    elif c == 2:
        resultado = SomaMDL.subtr(a,b)
        print("O resultado da subtração é {}".format(resultado))
        esc = int(input("Para finalizar o script digite 1, para continuar com as operações digite 2 "))
        if esc == 1:
                i = i+1
    elif c == 3:
        resultado = SomaMDL.mult(a,b)
        print("O resultado da multiplicação é {}".format(resultado))
        esc = int(input("Para finalizar o script digite 1, para continuar com as operações digite 2 "))
        if esc == 1:
                i = i+1
    elif c == 4:
        resultado = SomaMDL.divis(a,b)
        print("O resultado da divisão é {}".format(resultado))
        esc = int(input("Para finalizar o script digite 1, para continuar com as operações digite 2 "))
        if esc == 1:
                i = i+1

