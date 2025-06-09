i=1
Cla,Ed, Lo = [], [], []
while i==1:
    i = int(input("Você gostaria de prestar uma occorencia?\n1 - Sim\n2 - Não"))
    if(i==2):
        break
    b = int(input("-------\nInsira o tipo da ocorrencia\n-------\n1 - Direção perigosa   2 - Barulho\n3 - Bebedeira          4 - Homer\n"))
    c = int(input("-------\nInsira o grau da ocorrencia\n-------\n1 - Baixa   2 - media   3 - alta\n"))
    for i in range(1,3):
        contCLa, contEd, contLo = 0, 0, 0
        for i in range(len(Cla)):
            contCLa+=1
        for i in range(len(Cla)):
            contEd+=1
        for i in range(len(Cla)):
            contLo+=1
        if