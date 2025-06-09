alt = float(input("Insira o valor da Altura:  "))
peso = float(input("Insira o valor do peso em KG:  "))

IMC = peso/(alt**2)

if(IMC<=24.9):{
    print("O paciente tem peso normal, IMC: {:.2f}".format(IMC))
}
elif(IMC>24.9):
    print("O paciente tem sobrepeso, IMC: {:.2f}".format(IMC))