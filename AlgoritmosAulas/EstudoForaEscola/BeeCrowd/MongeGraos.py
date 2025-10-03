i = int(input(""))

while i>0:
    casas= int(input(""))
    ValorIn = 2.0
    for j in range(1,casas):
        ValorIn = ValorIn*2
    valorFat = ((ValorIn/12)/1000)
    print("{:.0f} kg".format(valorFat))
    i=i-1