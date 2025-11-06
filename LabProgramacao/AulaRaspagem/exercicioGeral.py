from random import randint
with open("clientes.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        i = (randint(1,4)/100)+(int(randint(0,10))/1000)
        linha = linha.strip()
        if linha == "":
            continue
        nome, valor = linha.split(";")
        PMT = int(valor)*((i*((i+1)**12))/(((i+1)**12)-1))
        print(f"{nome}\n FinanciamentoTotal:{valor} Juros:{i*100:.2f}% --> Parcela: {PMT:.2f}")