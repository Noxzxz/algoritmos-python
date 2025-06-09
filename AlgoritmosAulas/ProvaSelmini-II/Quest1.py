i=0
habA = int(input("Insira o numero de habitantes do País A: "))
habB = int(input("Insira o numero de habitantes do País B: "))

print("Insira a taxa de crescimento desta forma\nEx: 1.2(20%) , 1.5(50%), 1.05(5%)")
TaxA = float(input("Insira a taxa de crescimento do País A: "))
TaxB = float(input("Insira a taxa de crescimento do País B: "))

if(habA<habB and TaxA>TaxB):
    while(habA<habB):
        habA = habA+(habA*TaxA)
        habB = habB+(habB*TaxB)
        i+=1
    print("O numero de anos necessarios para que a população do País A ultrapasse o País B é {}".format(i))
else:
    print("Os dados inseridos estão desconexos")