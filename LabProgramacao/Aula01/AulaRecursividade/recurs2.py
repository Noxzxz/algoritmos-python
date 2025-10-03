#programa com função recursiva para ler um valor inteiro e positivo e retorne
# valor de fibonacci na posição indicada
def fibonnaci(a: int) -> int:
    if a == 1 or a == 2: return 1
    return fibonnaci(a-1) + fibonnaci(a-2)


def main():
    a = int(input("Insira a posição desejda: "))
    if a<0:
        print("Insira um valor positivo e inteiro")
    else:
        print(f'Posição {a} = {fibonnaci(a)}')
        
if __name__ == "__main__":
    main()