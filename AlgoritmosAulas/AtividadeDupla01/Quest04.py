QuantAnd = int(input("Digite a quantidade de andaimes disponíveis para locação: "))
ValorDia = float(input("Digite o valor diário do aluguel de cada andaime: "))

FatAlug = (ValorDia*(QuantAnd*1.2))*120

GanhoMult = (((QuantAnd*0.08)*ValorDia)*0.15)*5
GanhoMult2= ((QuantAnd*0.4*0.08)*ValorDia*0.15)*12


EstoqAnd = (QuantAnd*1.2)-(QuantAnd*0.05)

print("Faturamento anual com aluguéis: R$ {:.2f}\nGanho anual com multas: R$ {:.2f}\nQuantidade de andaimes ao final do ano: {:.0f}\n\n{:.2f}".format(FatAlug,GanhoMult,EstoqAnd,GanhoMult2))