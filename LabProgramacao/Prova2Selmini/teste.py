def filtrar(lista):
    qualificados = []
    i = 0
    while i < len(lista):
        linha = lista[i]
        pai = linha["pai"]
        filho = linha["filho"]
        tam_pai = len(pai)
        tam_filho = len(filho)
        
        condicao_valida = 1
        if tam_pai != tam_filho:
            condicao_valida = 0
        if tam_pai < 2 or tam_filho < 2:
            condicao_valida = 0

        if condicao_valida == 1:
            resultado, classificacao = verificar_compatibilidade(pai, filho)
        else:
            resultado, classificacao = "-", ""
        
        qualificados.append({
            "pai": pai,
            "filho": filho,
            "resultado": resultado,
            "classificacao": classificacao
        })
        i += 1
    return qualificados


def verificar_compatibilidade(pai, filho):
    acerto = 0
    tot = 0
    metade = int(len(pai) / 2)
    i = 0
    while i < metade:
        if pai[i] == filho[i]:
            acerto += 1
        tot += 1
        i += 1

    percentual = (acerto / tot) * 100
    classificacao = percentual > 80
    return percentual, classificacao


def main():
    listaPaiFilho = [
        {"pai": "AACCTGGA", "filho": "AAGCTGGT"},
        {"pai": "ACGTACGT", "filho": "ACGAACGA"},
        {"pai": "AGCTA", "filho": "AGGTA"},
        {"pai": "ACGTACGTACGTACG", "filho": "ACGTATGTACGTACG"},
        {"pai": "ACGTACGTACGTACG", "filho": "ACGAATGTACGTACG"},
        {"pai": "AACCTGGA", "filho": "AAGCTG"},
    ]
    
    listaResp = filtrar(listaPaiFilho)

    print("Possível Pai \t\t Filho \t\t Resultado \t\t Classificação")
    i = 0
    while i < len(listaResp):
        item = listaResp[i]
        print(item["pai"], end="\t\t")
        print(item["filho"], end="\t\t")
        print(item["resultado"], end="\t\t")
        if item["classificacao"] == True:
            print("POTENCIAL PAI-FILHO", end="\t\t")
        elif item["classificacao"] == False:
            print("NÃO COMPATÍVEL", end="\t\t")
        else:
            print("SEQUÊNCIAS DE TAMANHO INVÁLIDO", end="\t\t")
        print("")
        i += 1


if __name__ == "__main__":
    main()
