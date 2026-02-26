def filtrar(lista):
    qualificados = []
    for linha in lista:
        if len(linha.get('pai')) == len(linha.get("filho")) and len(linha.get('pai')) >=2 and len(linha.get("filho")) >=2:
            qualificados.append({
                "pai": linha.get("pai"),
                "filho": linha.get("filho"),
                "resultado": Compat(linha.get("pai"),linha.get("filho")),
                "classificacao": CompatBoolean(linha.get("pai"),linha.get("filho"))
            })
        else:
            qualificados.append({
                "pai": linha.get("pai"),
                "filho": linha.get("filho"),
                "resultado": "-",
                "classificacao": ""
            })
            
    return qualificados
        
#retorna porcentagem            
def Compat(Pai, filho):
    Acerto,tot = 0,0
    TmPai = int(len(Pai)/2)
    for i in range (TmPai):
        if Pai[i] == filho[i]:
            Acerto+=1
        tot+=1
    return (Acerto/tot)*100

#retorna true ou false
def CompatBoolean(Pai, filho):
    Acerto,tot = 0,0
    TmPai = int(len(Pai)/2)
    for i in range (TmPai):
        if Pai[i] == filho[i]:
            Acerto+=1
        tot+=1
    if((Acerto/tot)*100<80):
        return False
    if((Acerto/tot)*100>80):
        return True
                        
    
# função main
def main():
    listaPaiFilho = [
        {"pai":"AACCTGGA", "filho":"AAGCTGGT"},
        {"pai":"ACGTACGT", "filho":"ACGAACGA"},
        {"pai":"AGCTA", "filho":"AGGTA"},
        {"pai":"ACGTACGTACGTACG", "filho":"ACGTATGTACGTACG"},
        {"pai":"ACGTACGTACGTACG", "filho":"ACGAATGTACGTACG"},
        {"pai":"AACCTGGA", "filho":"AAGCTG"},
    ]
    
    listaResp = filtrar(listaPaiFilho)
    
    print("Possível Pai \t\t Filho \t\t Resultado \t\t Classificação")
    for i in  listaResp:
        print(i.get("pai"), end="\t\t")
        print(i.get("filho"), end="\t\t")
        print(i.get("resultado"), end="\t\t")
        if(i.get("classificacao")== True):
            print("POTENCIAL PAI-FILHO", end="\t\t")
        elif(i.get("classificacao")== False):
            print("NÃO COMPATÍVEL", end="\t\t")
        else:
            print("SEQUÊNCIAS DE TAMANHO INVÁLIDO", end="\t\t")
        print("")
        
# programa principal
if __name__ == '__main__':
    main()