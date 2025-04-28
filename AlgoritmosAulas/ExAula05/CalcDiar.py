Numdias = int(input("Insira o numero de diarias: "))

Valor1= Numdias*300

if(Numdias > 15):
    valor2 = 22.5*Numdias
elif(Numdias < 15):
    valor2 = 88.0*Numdias
elif(Numdias == 15):
    valor2 = 56.0*Numdias
    
total = Valor1+valor2
print("O valor pelos dias permanecidos será: {:.2f}".format(total))