i = 1
while i!=0:
    lad1 = int(input("Insira o valor do 1° lado: "))
    lad2 = int(input("Insira o valor do 1° lado: "))
    lad3 = int(input("Insira o valor do 1° lado: "))
    if(lad1 == 0 or lad2 == 0 or lad3 == 0):
        print("ALOMBADO (0_-_0)\nENCERRANDO OPERAÇÔES")
        i==0
        break
    if(lad1+ lad2 > lad3 and lad1+lad3> lad2 and lad2+lad3 > lad1):
        if(lad1==lad2 and lad1!= lad3):
            print("O triangulo é um triangulo isoceles")
        if(lad1==lad2 and lad1== lad3):
            print("O triangulo é um triangulo equilatero")
        if(lad1!=lad2 and lad1!= lad3):
            print("O triangulo é um triangulo escaleno")
    else:
        print("Não é um triangulo")
    