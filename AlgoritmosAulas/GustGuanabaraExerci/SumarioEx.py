import random
import BackCalcs
print("1 - NumReal 2 - CalcHipotenusa 3 - AngCalc\n4 - SortAlunos 5 - OrdemSort")
a = int(input("Insira o numero do script desejado:"))

if a == 1:
    num1 = float(input(" Insira o valor que sera transformado em real "))
    print("O valor real é {}".format(BackCalcs.NumReal(num1)))

elif a == 2:
    num1 = int(input("Insira o valor do cateto adjascente e cateto oposto do triangulo retangulo: "))
    num2 = int(input())
    print("O valor da hipotenusa é {}".format(BackCalcs.CalcHipot(num1,num2)))

elif a == 3:
    num1 = int(input("Insira o valor do angulo: "))
    print("O valor do cos é {:.3f}\nO valor do sen é {:.3f}\nO valor da tang é {:.3f}".format(BackCalcs.CalcAnglCos(num1), BackCalcs.CalcAnglSen(num1), BackCalcs.CalcAnglTang(num1)))

elif  a == 4:   
    nomes = []
    for i in range (4):
        nome = input("Nome do aluno {}: ".format(i+1))
        nomes.append(nome)
    sorteado = (BackCalcs.SortAluno())
    print("O aluno escolhido para limpar a lousa é {}".format(nomes[sorteado]))

elif a == 5:
    nomes = []
    ordemNomes = [] 
    for i in range (4):
        nome = input("Nome do aluno {}: ".format(i+1))
        nomes.append(nome)
    random.shuffle(nomes)
    print("A Ordem da apresentação é ")
    for nome in nomes:
        print(nome, end=" ,")
    