tupla = [(2,4),(1,3),(7,10),(3,6)]

inicio,fim = tupla[0]
for i in range(0,len(tupla)):
    a,b = tupla[i]
    if(a<fim):
        if(b>fim):
            fim = b
        if(a<inicio):
            inicio = a

            
print(inicio,fim)            
    
    
"""
def potencia(a,b: int) -> int:
    if b == 0: return 1
    return a*potencia(a,b-1)




def mult(m: int, n:int):
    if n>m:
        return mult(n,m)
    elif n == 1:
        return m
    return mult(m + m,n-1)


def main():
    m = int(input("Insira o 1° valor: "))
    n = int(input("Insira o 2° valor: "))

    print(f"mult({m},{n}) = {mult(m,n)}")
    
"""
    