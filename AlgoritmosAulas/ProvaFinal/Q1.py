qtd = int(input("Insira a quantidade de pacientes: "))
NmPac = []
TpCorp = []
PrsArt = []
RisPac = [0]*qtd

for i in range(0,qtd):
    NmPac.append(input("Insira o nome do {}º paciente: ".format(i+1)))
    TpCorp.append(float(input("Insira a temperatura corporal do paciente: ")))
    PrsArt.append(float(input("Insira a pressão arterial do paciente: ")))
    
def ImpresFebre(a,b,c):
    # qtd-> a TpCorp -> b NmPac ->c
    ListaFebre = ""    
    for i in range(0,a):
        if(b[i]>37.8):
            ListaFebre = ListaFebre+ ("\n{}     Temperatura Coportal: {}°C".format(c[i],b[i]))
    return print(ListaFebre)
        
for i in range(0,qtd):
    if(TpCorp[i]<=37.5 and PrsArt[i]<=130):
        RisPac[i] = "Baixo"
    elif((TpCorp[i]>=37.6 and TpCorp[i]<=38.5) or (PrsArt[i]>=131 and PrsArt[i]<=150)):
        RisPac[i] = "Moderado"
    elif(TpCorp[i]>38.5 or PrsArt[i]>150):
        RisPac[i] = "Alto"

def ImpresRisc(a,b,c):
    listaRisc = ""
    for i in range(0,a):
        listaRisc = listaRisc +("\n{}     risco: {}".format(c[i],b[i]))
    return print(listaRisc)
        
print("Os seguintes pacientes estão com febre\n------------------")
ImpresFebre(qtd,TpCorp,NmPac)
print("")
print("Listagem de Risco\n------------------")
ImpresRisc(qtd,RisPac,NmPac)