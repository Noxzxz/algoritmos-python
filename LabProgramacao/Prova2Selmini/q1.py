def VerificarRisada(risada):
    
    vogais = ["a","e","i","o","u"]
    IdaVog, esqVog = "",""
    
    #selecionar apenas vogais da esquerda pra direita
    for i in risada:
        if i.lower() in vogais:
            IdaVog+= i.lower()
            
    j= len(risada)-1
    #inverter string
    while j >= 0:
        esqVog += risada[j].lower()
        j-=1
    
    #selecionar apenas vogais da direita para a esquerda
    aux=""
    for i in esqVog:
        if i.lower() in vogais:
            aux+= i 
    
    #Compara strings
    if aux == IdaVog:
        return True   
    else:
        return False


def main():
    Resp = VerificarRisada(input("Insira a risada: "))

    if Resp == True:
        print("Valetina gostou")
    if Resp == False: 
        print("Valetina não gostou")

        
if __name__ == '__main__':
    main()