i = int(input("Insira o primeiro valor do parametro: "))
a = int(input("Insira o segundo valor do parametro: "))

for i in range(i, a+1):
    b=0
    c=1
    while  c<i:
        if(i%c==0):
            b=b+1
        c+=1
    if(b<2):
        print(i)