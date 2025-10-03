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
    

if __name__ =='__main__':
    main()