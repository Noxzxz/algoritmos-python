fat = int(input("Insira um valor:  "))

SomaRep = 0
while (fat>=1):
    SomaRep = SomaRep + (fat/(fat*(1/2))) 
    fat= fat - 1
    print(SomaRep)
    
    
print("A soma é {:.3f}".format(SomaRep))