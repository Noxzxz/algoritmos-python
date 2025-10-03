#Função para imprimir valores
def imprimir(n: int) -> None:
    while True:
        print(f"{n}",end=" ")
        if n==1:
            break
        if n%2 == 0:
            n = n//2
        else:
            n = (3*n)+1

#função principal --> main

def main ()->None:
    n = int(input("Insira um numero: "))
    imprimir(n)

#Programa principal
main()

'''
while(n!=1):
    print(n)
    if(n%2!=0):
        n = (3*n)+1
    else:
        n=n/2
        
print(n)'''