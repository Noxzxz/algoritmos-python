limite = int(input("Insira o valor limite"))

for temp in range(1, limite+1):
    total=0
    for i in range(1,temp):
        if temp%i == 0:
            total += i
            
    total_soma_div=0
    for i in range(1,total):
        if total%i==0:
            total_soma_div += i
    
    if(total_soma_div == temp):
        print("({} {})".format(total_soma_div,total), end=(""))