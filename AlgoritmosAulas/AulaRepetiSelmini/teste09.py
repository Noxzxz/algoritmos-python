cont = int(input("Insira a quantidade de produtos"))
somaVAL=0
for i in range (cont):
    produto = float(input("Insira o valor do produto {}°: ".format(i)))
    somaVAL = somaVAL + produto

formaPag = int(input("Insira a forma de pagamento\n1 - A vista com desconto de 10%\n2 - Em duas vezes com acrescimo de 15.5%\n "))
if(formaPag == 1):
    print("O valor total a ser pago é R${:.3f}".format(somaVAL*0.9))
elif(formaPag == 2):
    print("O valor total a ser pago é R${:.3f}".format(somaVAL*1.155))
else:
    print("Insira um valor valido")