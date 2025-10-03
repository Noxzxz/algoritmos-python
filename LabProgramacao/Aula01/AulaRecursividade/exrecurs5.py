def fatDuplo(m: int, n:int):
    if m<2:
        return n
    return fatDuplo(m-2,n+m)


def main():
    m = int(input("Insira um valor: "))

    print(f"fatDuplo({m}) = {fatDuplo(m,0)}")
    

if __name__ =='__main__':
    main()