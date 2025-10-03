posiInt = int(input("Insira um valor inteiro e positivo: "))

if(posiInt>0):
    print("O valor inserido é divisivel por ")
    for i in range (posiInt):
        if ((posiInt % int(i +1))==0):
            print("{}, {}".format(i+1, -(i+1)))