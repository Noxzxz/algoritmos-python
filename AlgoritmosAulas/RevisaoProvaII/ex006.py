import ex001_util;
qtd = int(input("Insira o numero de meses: "))
NmMeses = []
VlTemp = []
for i in range(0,qtd):
    NmMeses.append(input("Insira o nome do mês: "))
    VlTemp.append(int(input("Insira a media da temperatura: ")))

MediaTemp = ex001_util.calcular_media(VlTemp)
print("A media de temperatura dos meses inseridos foi {:.2f}".format(MediaTemp))