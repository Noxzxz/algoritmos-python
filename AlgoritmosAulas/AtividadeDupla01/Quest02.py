MontanteP = float(input("insira o montante inicial investido: "))

TaxaJuro = float(input("Insira o valor da taxa de juro: "))
if (TaxaJuro>1 and TaxaJuro< 0):
    TaxaJuro = float(input("Insira um valor de taxa de juro valido( entre 0 e 1): "))
elif(TaxaJuro>1 and TaxaJuro< 0):
    TaxaJuro = float(input("Insira um valor de taxa de juro valido( entre 0 e 1): "))
    
NumMese = int(input("Insira o numero de meses do investimento:"))

Alg1 = (1+TaxaJuro)**NumMese
TotResult = ((Alg1 - 1)/TaxaJuro)*MontanteP

print("O valor acumulado é: {:.2f}".format(TotResult))