#Alternativa A
def TotChuva(tupla):
    nm, manha, noite = tupla
    tot = manha+noite
    return tot

def Diferença(tupla):
    nm, manha, noite = tupla
    tot = manha-noite
    if(tot<0):
        tot = (noite- manha)
    return tot
    
#Função Resumo Dia
def ResumDia(tupla):
    listaRes = []
    for i in tupla:
        listaRes.append([i[0], TotChuva(i),Diferença(i)])
    return listaRes

#Função maior dia de consumo
def MaiorTor(tupla):
    NmMaior, NumMaior = tupla[0][0],tupla[0][1]
    for i in tupla:
        if NumMaior < i[1]:
            NmMaior, NumMaior = i[0],i[1]
    return NmMaior
    


def main():
    dias = int(input("Insira o numero de dias"))

    lista = []
    for i in range(dias):
        linha = []
        linha.append(input("Insira da data: "),)
        linha.append(float(input("Insira o consumo de agua no periodo da manha: ")))
        linha.append(float(input("Insira o consumo de agua no periodo da noite: ")))
        lista.append(linha)
    
    lista = tuple(lista)
    print(lista)
    
    print("Total de consumo primeiro: ",TotChuva(lista[0]))

    #Resposta Questões
    print("Resumo dos dias: \n",ResumDia(lista))

    ResumoDia = ResumDia(lista)

    print("Data de maior consumo: ",MaiorTor(ResumoDia))
    

if __name__ == "__main__":
    main()