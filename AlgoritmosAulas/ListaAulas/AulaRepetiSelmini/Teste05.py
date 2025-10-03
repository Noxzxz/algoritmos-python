fat = int(input("Insira um valor:  "))

SomaRep = 0
while (fat>=1):
    SomaRep = SomaRep + (1/fat) 
    fat= fat - 1
    print(SomaRep)
    
    
print("A soma é {:.3f}".format(SomaRep))