a = input("Insira um numero binario: ")
numD = 0

for i in a:
    if (int(i) == 0 or int(i) ==1) : 
        bin = True
    else:
        bin = False
        break
    
        
if bin:
    for i in range(len(a)):
        numD += int(a[-(i+1)]) * (2**i)
    print("O numero em decimal é {}".format(numD))
else: 
    print("Insira um numero valido")