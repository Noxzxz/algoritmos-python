from random import randint

m = [[ randint(0,10) for j in range(4)] for i in range(4)]

for i in range(len(m)):
    for j in range (len(m)):
        print(m[i][j],end="\t")
    print("\n")
    
contador = 0
for i in range(len(m)):
    for j in range (len(m)):
        if((i+j) == (len(m)-1)):
            aux = m[contador][contador]
            m[contador][contador] = m[i][j]
            m[i][j] = aux
            contador+=1
            
            
print("Revelação")
for i in range(len(m)):
    for j in range (len(m)):
        print(m[i][j],end="\t")
    print("\n")

