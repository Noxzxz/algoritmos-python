import math
pi= 3.14159265

altH = float(input("Digite a altura do reservatório (em metros): "))
raioCil = float(input("Digite o raio do reservatório (em metros): "))
valorUnid = float(input("Digite o custo de cada unidade de isolamento: "))

AreaTot= (2*pi*raioCil*(raioCil+altH))
Quant = math.ceil(AreaTot/(3*0.95))
CustTot = Quant*valorUnid

print("Área total a ser isolada: {:.2f} m²\nQuantidade de unidades de isolamento: {}\nCusto total: R$ {:.2f}".format(AreaTot, Quant,CustTot))
