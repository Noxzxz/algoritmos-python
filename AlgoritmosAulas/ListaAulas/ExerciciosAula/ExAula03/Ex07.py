x = int(input("Insira um valor para a equação: "))

first = ((x **4 - 1) / (2* x ** 2))**2
second = (1+first)**(1/2)
third = second - (x ** 2)/2


# a= ((1 + (((x ** 4) - 1)/(2 * x ** 2 ))) ** (1/2)) - ((x ** 2)/2)

print('O resultado da equação é {:.5f}'.format(third))