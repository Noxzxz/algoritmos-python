QuantB= int(input("Insira a quantidade de bicicletas: "))
ValorB= int(input("Insira o valor do aluguel das bicicletas: "))

FatAn=  ((QuantB*(1/3))*ValorB)*365
Multa = ((((QuantB*(1/3))*0.1)*ValorB)*0.1)*365

print("Faturamento anual: {:.2f}\nGanho com multas anual: {:.2f}".format(FatAn,Multa))