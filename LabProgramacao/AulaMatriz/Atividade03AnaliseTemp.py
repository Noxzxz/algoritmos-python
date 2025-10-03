from random import randint

def gerarMatriz():
    m = [[randint(-10,50) for i in range(10)]for j in range(12)]
    return m

def impresMatriz(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end="\t")
        print("")
        
def impresLista(a):
    for i in range(len(a)):
            print(f"Ano {i+1}º: {a[i]:.2f}")
    print("")
        
def listaMediaAno(a):
    b = []
    for i in range(len(a)):
        somaMedia=0
        for j in range (len(a[0])):
            somaMedia += a[i][j]
        b.append(somaMedia/len(a[0]))
    return b

def MaiorMenor(a):
    for i in range(len(a)):
        menor = a[0]
        menorAno = 0
        maior = a[0]
        maiorAno = 0
        if menor>a[i]:
            menor = a[i]
            menorAno = i
        if maior<a[i]:
            maior = a[i]
            maiorAno = i
    return print(f"O {menorAno+1}º teve a menor media com {menor:.2f}\nO {maiorAno+1}º teve a maior media com {maior:.2f}")
                
            
#Codigo Bruto

def main():
    m = gerarMatriz()
    impresMatriz(m) 
    SomaMedia = listaMediaAno(m)
    impresLista(SomaMedia)
    MaiorMenor(SomaMedia)

if __name__ == "__main__":
    main()