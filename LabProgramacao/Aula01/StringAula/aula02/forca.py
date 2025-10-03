import random

palavras = []

numero = int(input("Insira a quantidade de palavras"))
for i in range (numero):
    palavras.append(input(f"Insira a palavra {i}: "))

print(palavras)

palavraEsc= random.choice(palavras)
erro = 0
while erro<=6:
    textoInsert = input("Insira uma letra: ")
    #textoInsert.append(input("Insira uma letra: "))
    for i in palavraEsc:
        if textoInsert == i:
            print("Certo")
            print