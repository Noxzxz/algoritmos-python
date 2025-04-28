temp = 0 
while temp < 1:
    i = 0
    a = int(input("Insira um valor: "))
    while i < 11:
        print("{} X {} =  {}".format(a,i, a*i))
        i = i +1
    temp = int(input("0 - Continuar    1 - Sair"))