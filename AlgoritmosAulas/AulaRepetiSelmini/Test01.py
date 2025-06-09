val1 = int(input(f"Insira o 1° valor: "))
val2 = int(input(f"Insira o 2° valor: "))

if(val1>val2):
    while val2 <= val1:
        if((val2%2) == 0):
            print(val2)
        val2= val2 + 1
elif(val1<val2):
    while val2 >= val1:
        if((val1%2) == 0):
            print(val1)
        val1 = val1+ 1


print("ACABOU")