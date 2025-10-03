from math import sqrt


x=0

while(x>=-5 and x<=5):
    x = int(input("Insira o valor de x(O valor de x deve ser maior que 5): "))

Calc= (x-8)/((x**2-25)**(1/2))
print("O valor da equação é {:.3f}".format(Calc))
    