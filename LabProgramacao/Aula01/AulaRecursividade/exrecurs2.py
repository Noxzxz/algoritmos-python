def somaDigi(a) -> int:
    if a == 0: return 0
    return a % 10 + somaDigi(a//10)

def main():
    a = int(input("Insira um numero: "))
    if a<0:
        print("Insira um valor positivo e inteiro")
    else:
        print(f'Resultado {a} = {somaDigi(a)}')
        
if __name__ == "__main__":
    main()