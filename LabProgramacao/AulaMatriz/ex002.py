from random import randint

m = [[ randint(0,10) for j in range(4)] for i in range(4)]

for i in range(4):
    for j in range (4):
        print(m[i][j],end=" ")
    print("")


for i in range(4):
    m[i].append(m[i][0] + m[i][1]+ m[i][2]+ m[i][3])
    

# Cria uma terceira linha com as somas das colunas
linha_somas = [
    m[0][0] + m[1][0]+ m[2][0] + m[3][0],
    m[0][1] + m[1][1] + m[2][1] + m[3][1],
    m[0][2] + m[1][2] +m[2][2] + m[3][2],
    m[0][3] + m[1][3] +m[2][3] + m[3][3],
    m[0][0] + m[1][1] +m[2][2] + m[3][3]
]
m.append(linha_somas)

print("")

for i in range(5):
    if(i>3):
            print("----------------------------------")
    for j in range (5):
        if(j==4 and i!=4):
            print(" | ",end="")
        print(m[i][j],end="\t")
    print("")


