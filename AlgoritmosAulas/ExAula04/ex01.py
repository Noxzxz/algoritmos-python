#Validação de nota

nota1 = float(input("Insira o valor da sua 1º nota: "))
nota2 = float(input("Insira o valor da sua 2º nota: "))

media =(nota1+nota2)/2

print("Media: {:.2f}".format(media))

if(media >= 7):
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!!!!!!!")
