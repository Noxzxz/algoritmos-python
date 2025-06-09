num = int(input("Insira um numero: "))

somaD, fat=0, 1

for i in range(1,num+1):
    fat = fat*i 

print("O valor do fatorial é",fat)

while fat>0:
    somaD += fat%10
    fat= fat//10

print("A soma dos digitos do fatorial é",somaD)