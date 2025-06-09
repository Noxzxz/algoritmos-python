n = int(input("Qual a quantidade de pontos que serão informados?\n---> "))

for i in range(n):
    print("Ponto {}:".format(i+1))
    cord1 = int(input("x -->"))
    cord2 = int(input("y -->"))
    print("Distância até a origem --> {:.4f}".format(((0 - cord1)**2 + (0-cord2)**2)**(1/2)))
    if(i==0):
        maior = ((0 - cord1)**2 + (0-cord2)**2)**(1/2)
        menorcord1, menorcord2 = cord1,cord2
        menor = ((0 - cord1)**2 + (0-cord2)**2)**(1/2)
        maiorcord1, maiorcord2 = cord1,cord2
        
    if(menor>((0 - cord1)**2 + (0-cord2)**2)**(1/2)):
        menor = ((0 - cord1)**2 + (0-cord2)**2)**(1/2)
        menorcord1, menorcord2 = cord1,cord2
        
    if(maior<((0 - cord1)**2 + (0-cord2)**2)**(1/2)):
        maior = ((0 - cord1)**2 + (0-cord2)**2)**(1/2)
        maiorcord1, maiorcord2 = cord1,cord2

print("O ponto mais distante tem coordenadas --> ({}, {})\nO ponto mais perto tem coordenadas --> ({}, {})\n".format(maiorcord1,maiorcord2,menorcord1,menorcord2))

    
    