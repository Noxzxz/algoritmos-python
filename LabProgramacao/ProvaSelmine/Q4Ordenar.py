import time
#CODIGO ALUNO CHATO
def ordernar(x):
    n = len(x)
    if n<2:
        return
    
    indice_menor = 0
    i = 1
    while i<n:
        if x[i]< x[indice_menor]:
            indice_menor = i
        i += 1
    x[0], x[indice_menor] = x[indice_menor], x[0]
    
    i=2
    while i<n:
        chave = x[i]
        if chave >= x[i-1]:
            i+=1
            continue
        j = i
        while x[j-1]> chave:
            x[j] = x[j-1]
            j-= 1
        x[j] = chave
        i += 1


#QUICKA SORT
def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
        
    if inicio < fim:
        pivo = particionar(lista, inicio, fim)
        quicksort(lista, inicio, pivo - 1)
        quicksort(lista, pivo + 1, fim)

def particionar(lista, inicio, fim) -> int:  # retorna o índice do pivô
    pivo = lista[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    # coloca o pivô no local correto
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1


lista = [3, 3, 4, 5, 5, 6, 7, 8, 8]

def medir_tempo(algoritmo, lista:list) -> float:
    lista_aux = lista.copy()
    inicio = time.perf_counter()
    algoritmo(lista_aux)
    fim = time.perf_counter()
    return(fim-inicio) * 1000

Tempo_AlunoOrdenar = medir_tempo(ordernar, lista)
tempo_quickSort = medir_tempo(quicksort, lista)

print(f'Tempo Aluno ordenar {Tempo_AlunoOrdenar:.3f}')
print(f'Tempo quickSort {tempo_quickSort:.3f}')