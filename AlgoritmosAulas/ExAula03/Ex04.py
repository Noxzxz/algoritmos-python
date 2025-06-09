from tokenize import Double

salMin = int(input('Insira o valor do salario minimo: '))
Kwats = int(input('Insira o valor gasto de kilowats: '))

KiloPrec = (salMin/7)/100
Cont = Kwats*KiloPrec
ContDesc = Cont-(Cont*0.1)

print('O valor do Kilowats é {:.4}, O valor a ser pago pela residencia é {:.4} \nO valor a ser pago pela residencia apos o desconto de 10% é {:.4}'.format(KiloPrec, Cont,ContDesc))