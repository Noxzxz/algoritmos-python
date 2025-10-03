cart = int(input(""))
baralho = [i for i in range(cart)]
i=0
while i<cart:
    print(baralho[i])
    i+=1
    
baralhoEmb = (i for i in range(cart))


while baralhoEmb[cart/2] != baralho[cart/2] and baralho[cart] != baralhoEmb[cart]:
    aux = baralhoEmb[cart/2]
    baralhoEmb[cart]
    

