
valH = float(input('Insira o valor da hora do professor: '))
trabH = float(input('Insira o numero de horas trabalhadas: '))
Inss = float(input('Insira o valor do INSS: '))

salBrut = valH*trabH
salLiq = salBrut - Inss

print('\n\nO salario bruto é {:.2f}\nO salario liquido é {:.2f}'.format(salBrut,salLiq))