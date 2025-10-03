def mdc(m: int, n:int):
    if n>m:
        return mdc(n,m)
    elif n == 0:
        return m
    return mdc(n,m % n)


def main():
    m = int(input("Insira o 1° valor: "))
    n = int(input("Insira o 2° valor: "))

    print(f"mdc({m},{n}) = {mdc(m,n)}")
    

if __name__ =='__main__':
    main()