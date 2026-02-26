import util
"""
def estranho(A, x,l,r,depth = 0):
    if l>r:
        return -1
    if depth % 2 == 0:
        if A[l] == x:
            return l
        if A[r] ==x:
            return r
    else:
        if A[r] == x:
            return r
        if A[l] == x:
            return l
    return estranho(A,x,l+1,r-1,depth+1), depth

A = [9, 6, 8, 0, 7, 1, 5, 4, 2, 3, 10]

print(estranho(A, 4, 0, len(A)-1))

def estranho(A, x, i=0, passo=1):
    if i >= len(A):
        return -1
    
    achou = (A[i] == x)
    r = estranho(A,x, i+passo, passo+1)
    if r != -1:
        return r
    if achou:
        return i
    return -1


def estranho(A,x, ini, fim):
    if ini >= fim:
        return ini if A[ini] >= x else ini+1
    meio = (ini+fim)//2
    if A[meio]< x:
        return estranho(A,x,meio+1, fim)
    else:
        return estranho(A,x, ini, meio)
    
A = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8]
x = 4

print(estranho(A,x,0,7))


def bolha(lista: list[int]) -> list[int]:
    for j in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        print(lista)
    return lista

bolha([64, 34, 25, 12, 22, 11, 90])

A = [17, 18, 90, 5, 76, 3, 2, 15]

def estranho(A):
    if len(A) <=1:
        return A
    p = A[0]
    L = [x for x in A[1:] if x <p]
    E = [x for x in A if x ==p]
    G = [x for x in A[1:] if x >p]
    return estranho(G) + E + estranho(L) 

print(estranho(A))

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
"""

def estranho(A):
    n = len(A)
    size = 1
    B = A[:]
    while size < n:
        for start in range(0, n, 2*size):
            mid = min(start + size, n)
            end = min(start + 2*size, n)
            i, j = start, mid
            k = start
            while i < mid and j < end:
                if B[i] <= B[j]:
                    A[k] = B[i]
                    i += 1
                else:
                    A[k] = B[j]
                    j += 1
                k += 1
            while i < mid:
                A[k] = B[i]
                i += 1
                k += 1
        B = A[:]
        size *= 2
    return A


print(estranho([85,24,63,45,17,31,96,50]))