NmAct = []
VlActBt = []
VlActFc = []

a = int(input("Insira o numero de ações: "))
for i in range(0,a):
    NmAct.append(input("Insira o nome da ação"))
    VlActBt.append(float(input("Insira o valor da ação na abertura: ")))
    VlActFc.append(float(input("Insira o valor da ação no fechamento: ")))
    
def Variação(b,c):
    #b ->VlactBt c-> VlActFc
    variacao = ((c-b)/b)*100
    return variacao

print("A lista de variação\n-------------------------------------")
for i in range(0,a):
    print("{}        {:.2f}%".format(NmAct[i],Variação(VlActBt[i],VlActFc[i])))
print("-------------------------------------")
    
def SimulInvest(b,c):
    ValFim = (1000*(1+(Variação(b,c)/100)))
    return ValFim

ValFim=[]
for i in range(0,a):
    ValFim.append(SimulInvest(VlActBt[i],VlActFc[i]))

for j in range(0,a):
    for i in range(0,a-1):
        if(ValFim[i]<ValFim[i+1]):
            auxVL=ValFim[i]
            auxNm=NmAct[i]
            ValFim[i] = ValFim[i+1]
            NmAct[i] = NmAct[i+1]
            ValFim[i+1] = auxVL
            NmAct[i+1] = auxNm
            

print("Lista de simulação das Ações\n-------------------------------------")
for i in range(0,a):
    print("Nome: {}     Valor: {:.2f}".format(NmAct[i],ValFim[i]))
print("-------------------------------------")
print("A ação mais lucrativa do dia: {}".format(NmAct[0]))
print("A ação menos lucrativa do dia: {}".format(NmAct[a-1]))
print("-------------------------------------")
    

    
    