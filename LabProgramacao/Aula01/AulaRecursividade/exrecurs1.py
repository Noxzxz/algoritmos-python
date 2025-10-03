def potencia(a,b: int) -> int:
    if b == 0: return 1
    return a*potencia(a,b-1)

def main():
    a = int(input("Insira um numero: "))
    b = int(input("Insira a potencia desse numero: "))
    if b<0:
        print("Insira um valor positivo e inteiro")
    else:
        print(f'Resultado {a}^{b} = {potencia(a,b)}')
        
if __name__ == "__main__":
    main()