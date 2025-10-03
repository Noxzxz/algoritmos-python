i= 0
carregado = []
while(i==0 or i>4) or i<0:
   i = int(input("Insira o valor referente ao nivel\n 1º Facil\n 2º Normal\n 3º Dificl\n 4º TryHard\n"))

nvl1 = 'gato'
nvl2 = 'bosque'
nvl3 = 'advogado'
nvl4 = 'afta'

if(i==1): #nivel facil
        certo = 0
        while(i<=6 and i>0):#6 tentativas de chute de palavra ou letra
            print(nvl1)
            Esc = int(input("Escolha entre um chute a palavra completa 1º e chutar apenas 1 letra 2º\n"))
            if(Esc==1): #Visualizer palavra completa
                PalChute = input("Insira a palavra completa:  ")
                if(PalChute == nvl1):
                    print("Parabens você acertou")
                else:
                    print("Resposta Incorreta")
                i+=1
            elif(Esc == 2): #Visualizer letra unitaria
                LetraChute = input("Insira apenas 1 letra da palavra:  ")
                carregado += [LetraChute]
                for temp in nvl1:
                    if(temp == str.lower(LetraChute)):
                        print("Há a ocorrencia da letra '{}' na palavra".format(str.lower(LetraChute)))
                i+=1
                if(certo<=0):
                        certo +=1
                elif(certo>=1):
                    for Cont in carregado:
                        if(Cont != LetraChute):
                            certo +=1
                        else:
                            print("Essa letra ja foi constatada")
            if(certo>4):
                print("Todas as plavras foram constatadas\nParabéns vc é foda, ou quase isso\nA palavra é gato")
                    

print("Tudo certo pai")