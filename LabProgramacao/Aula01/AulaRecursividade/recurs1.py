# função recursiva para calcular o fatorial de um numero inteiro positivo

def fatorial (a: int) -> int:
    if a == 0:return 1
    return a*fatorial(a-1)
    
#função principal
def main():
    a = int(input("Insira um valor: "))
    if a<0:
        print("O valor deve ser inteiro e positivo")
    else:
        print(f"{a}! = {fatorial(a)}")

#programa principal
if __name__ == '__main__':
    main()