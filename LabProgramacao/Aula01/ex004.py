#def eh_primo(valor: int) -> bool:
     

def gerar_primos(n: int) ->list:
    lista = []
    valor = 2
    while len(lista)<n:
        if eh_primo(valor):
            lista.append(valor)
        valor = valor+1
    return lista


def main () ->None:
    n = int(input("Informe a quantidade de números primos: "))    