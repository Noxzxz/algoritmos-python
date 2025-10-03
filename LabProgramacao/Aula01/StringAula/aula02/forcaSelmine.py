import random

def LerPalavras():
    palavras = []
    for i in range(5):
        palavras.append(input(f"Insira a palavra {i+1}º: "))
    return palavras

def jogar(a):
    #lista auxiliar
    Testes= ["_"]*len(a)
    
    erro = 0
    while erro<= 6 and "_" in Testes:
        print(Testes)
        textoInsert = input("Insira uma letra: ")
        
        if textoInsert in a:
            for i in range(len(a)):
                if textoInsert == a[i]:
                    Testes[i] = textoInsert
        else:
            erro+=1
            print(f"Você errou pela {erro}ª vez. Tente Novamente!")
    
    if "_" not in Testes:
        print("Você é o megamente")
    else:
        print("Você foi enforcado\nMuiTo BurROoo kKKKKKkkkkkkkkkkkkkkkkkkKKK")
        

def main():
    palavras = LerPalavras()
    palavraEsc = random.choice(palavras)
    jogar(palavraEsc)
    
    
if __name__ == '__main__':
    main()