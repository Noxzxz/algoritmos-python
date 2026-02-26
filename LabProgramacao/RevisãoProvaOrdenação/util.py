"""
ordenação interna: os dados a serem ordenados “cabem” na memória principal.
ordenação externa: os dados a serem ordenados estão armazenados em memória
secundária (discos externos).
"""

# função para realizar a busca linear (sequencial) em uma lista numérica. A função
# deve receber como parâmetro a lista e o valor a ser localizado. A função retorna o índice
# do elemento encontrado ou, caso contrário, retorna -1
"""busca sequencial simples, verifica um por um (O(n)), ideal para listas pequenas ou desordenadas"""
def busca_sequencial(lista: list[int], valor: int) -> int:
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  
    return -1  

#---------------------------------------------------------------------------------------------------
# função que realiza a busca binária em uma lista ordenada (a lista tem que estar ordenada)
# a função recebe como parâmetro a lista e também o valor a ser pesquisado. Se o valor for
# encontrado, a função retorna o índice. Se não for encontrado retorna -1.
#busca binária muito mais rápida (O(log n)), mas exige que a lista esteja ordenada, dividindo o problema pela metade a cada passo para descartar grande parte dos dados. 
def busca_binaria(lista: list[int], valor):
    ini, fim = 0, len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1

#------------------------------------------------------------------------------------------------
# função para ordenar uma lista de números inteiros em ordem crescente usando o método
# bolha (bubblesort)
"""
Dentre os métodos de ordenação é o método de classificação (ordenação)
menos eficiente.

O método consiste em percorrer um array ou uma lista sequencialmente várias vezes. A
cada passagem pelo array (lista) compara-se cada elemento com o seu sucessor (𝑥𝑥[𝑖𝑖]
com 𝑥𝑥[𝑖𝑖 + 1]) e troca-se os dois elementos se eles não estiverem na ordem correta.
"""
def bolha(lista: list[int]) -> list[int]:
    for j in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

#-----------------------------------------------------------------------------------------------
# função para ordenar uma lista pelo método da seleção
"""
A cada etapa realizada, é identificado o menor (ou o maior) elemento dentro do segmento que
contém os elementos ainda não selecionados.
 É realizada uma troca do elemento identificado na etapa anterior com o primeiro elemento do
segmento.
 O tamanho do segmento é atualizado, ou seja, subtrai-se um do tamanho do segmento (menos
um elemento).
 O processo é interrompido no momento em que o segmento ficar com apenas um elemento.

"""
def selecao(x):
    n = len(x)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if x[j] < x[menor]:
                menor = j

        # Troca os elementos (essa linha precisa estar dentro do laço externo)
        x[i], x[menor] = x[menor], x[i]

#---------------------------------------------------------------------------------------------
# função para ordenar uma lista pelo método de inserção
"""
Existe a divisão do array (lista) lista a ser ordenado em dois segmentos: o primeiro contendo
os elementos já ordenados e o segundo contendo os elementos ainda não ordenados.
Descrição do algoritmo:
 Um primeiro elemento está no array (lista) ordenado e os demais no array (lista) desordenado.
 Retira-se o primeiro elemento do array (lista) desordenado. Ao colocá-lo no segmento ordenado é
realizada a devida comparação para inseri-lo na sua posição correta.
 Repete-se o processo até que todos os elementos do segmento desordenado tenham passado
para o segmento ordenado.
"""
def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
        x[i + 1] = valor


#--------------------------------------------------------------------------------------
# função para ordenar uma lista pelo método quicksort (pivô como último elemento)
"""É um algoritmo de ordenação rápida que usa a estratégia de divisão e conquista. É o
algoritmo de ordenação mais utilizado do mundo. Por usar a estratégia de divisão e conquista é um algoritmo recursivo.


1. Escolha um elemento da lista, denominado pivô.
2. Particiona: rearranje a lista de forma que todos os elementos anteriores ao pivô
sejam menores que ele, e todos os elementos posteriores ao pivô sejam maiores
que ele. Ao fim do processo o pivô estará em sua posição final e haverá duas sub
listas não ordenadas. Essa operação é denominada partição.
3. De forma recursiva, ordene a sub lista dos elementos menores e a sub lista dos
elementos maiores.

"""
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

#--------------------------------------------------------------------
# algoritmo de ordenação mergesort
"""
É um algoritmo de ordenação por intercalação de elementos que usa a estratégia de
divisão e conquista.
1. Dividir: calcula o ponto médio do array;
2. Conquistar: de forma recursiva resolve dois subproblemas, cada um de tamanho
n / 2, onde n é a quantidade de elementos do array que será ordenado;
3. Combinar: Unir os “sub arrays” em um único conjunto ordenado.

"""
def mergesort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    esquerda_ordenada = mergesort(esquerda)
    direita_ordenada = mergesort(direita)
    
    return juntar_listas(esquerda_ordenada, direita_ordenada)


def juntar_listas(esq, dir):
    i = 0  # índice da lista da esquerda (para ninguém fazer confusão entre os índices)
    j = 0  # índice da lista da direita
    resultado = []
    
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    # cuidado: é importante verificar se sobre algum elemento na 
    # lista da esquerda ou na da direita. Se sobrar algum elemento,
    # acrescenta no final da lista
    while i < len(esq):
        resultado.append(esq[i])
        i += 1

    while j < len(dir):
        resultado.append(dir[j])
        j += 1

    return resultado