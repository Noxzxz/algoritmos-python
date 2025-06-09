qtd = int(input("Insira o numero de produtos: "))
NmProd = []
VlProd = []
for i in range(0,qtd):
    NmProd.append(input("Insira o nome do {} produto: ".format(i+1)))
    VlProd.append(int(input("Insira o valor do produto: ")))

for j in range(1,len(VlProd)):
    for i in range(0,len(VlProd)-1):
        if(VlProd[i]>VlProd[i+1]):
            auxVL=VlProd[i]
            auxNm=NmProd[i]
            VlProd[i] = VlProd[i+1]
            NmProd[i] = NmProd[i+1]
            VlProd[i+1] = auxVL
            NmProd[i+1] = auxNm


print("Lista dos Produtos\n-------------------------------------")
for i in range(0,len(VlProd)):
    print("Nome: {}     Valor: {}".format(NmProd[i],VlProd[i]))
print("-------------------------------------")

