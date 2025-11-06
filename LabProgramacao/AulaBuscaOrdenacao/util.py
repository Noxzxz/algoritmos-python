#Função para realizar a busca linear em uma lista numerica.
#A função deve receber como parametro a lista e o valor a ser localizado.

def ProcurarLista(list,alvo):
    for i in range (len(list)):
        if list[i] == alvo:
            local = i
            break
    return local+1

def OrdenarLista(list):
    n =len(list)
    for i in range(n-1):
        for j in range(n-1-i):
            if list[j]>list[j+1]:
                list[j], list[j+1]= list[j+1], list[j]
    return list

def ProcurarMelhorLista(list,alvo):
    list = OrdenarLista(list)
    met = int(len(list)/2)
    local = 0
    if list[met]<alvo:
        for i in range(met, len(list)):
            if list[i] == alvo:
                local = i
                break
    else:
        for i in range(0,met):
            if list[i] == alvo:
                local = i
                break
    return local+1
    