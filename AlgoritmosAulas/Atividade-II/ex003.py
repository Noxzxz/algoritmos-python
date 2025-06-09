QtdAlunos = int(input("Insira o numero de alunos partcipantes da pesquisa: "))

favor, contra=0,0
for i in range(1, QtdAlunos+1):
    a = int(input("insira a opinião do participante sobre o projeto\n1 - A favor\n2 - Contra\n"))
    if(a==1):
        favor+=1
    elif(a==2):
        contra+=1

print("O numero de participante é {}\nO numero de participante a favor é {}\nO numero de participantes contra é {}".format(QtdAlunos, favor, contra))
print("A porcetagem de alunos a favor é {}%\nA porcentagem de alunos que são contra é {}%".format((favor/QtdAlunos)*100,(contra/QtdAlunos)*100))