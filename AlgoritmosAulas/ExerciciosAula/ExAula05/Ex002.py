a = float(input("Insira a nota da 1° prova: "))
b = float(input("Insira a nota da 2° prova: "))

c = float(input("Insira a nota do 1° trabalho: "))
d = float(input("Insira a nota do 2° trabalho: "))

mediaNota = ((a+b)/2)*0.7 + ((c+d)/2)*0.3   

print('A media é: {:.2f}'.format(mediaNota))
if(mediaNota >= 7):
    print('O aluno foi aprovado')
else:
        print('O aluno foi reprovado')