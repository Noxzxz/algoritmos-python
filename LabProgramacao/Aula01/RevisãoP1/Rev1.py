def matriz(a,b):
    matriz = [[i+j for i in range(a)]for j in range(b)]
    return matriz

def imprimir(a):
    for i in range(len(a)): #percorre linha
        for j in range(len(a[0])): #percorre coluna
            print(a[i][j], end="\t")
        print("")
        
a = matriz(3,3)
imprimir(a)
print(a[1][1],a[0][1],a[2][1])

def fib(a):
    if a==1 or a == 2: return 1
    return fib(a-1) + fib(a-2)
print(fib(3), fib(5), fib(1),"caralhoo")