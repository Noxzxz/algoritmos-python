fat = int(input("Insira um valor:  "))

SomaRep = 0
for i in range(fat):
    SomaRep = SomaRep + (1/(i+1))
    print(SomaRep)
    
    
print("A soma é {:.3f}".format(SomaRep))