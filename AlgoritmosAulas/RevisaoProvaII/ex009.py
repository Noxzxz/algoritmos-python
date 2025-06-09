import random

# Entradas do usuário
tamanho = int(input("Informe a quantidade de elementos em cada lista: "))
min_valor = int(input("Informe o valor mínimo para os números aleatórios: "))
max_valor = int(input("Informe o valor máximo para os números aleatórios: "))

# Geração das duas listas com números aleatórios
lista1 = [random.randint(min_valor, max_valor) for _ in range(tamanho)]
lista2 = [random.randint(min_valor, max_valor) for _ in range(tamanho)]

# Impressão das listas geradas
print("\nLista 1:", lista1)
print("Lista 2:", lista2)

# Gerando a lista de interseção sem repetições
intersecao = []

for num in lista1:
    if num in lista2 and num not in intersecao:
        intersecao.append(num)

# Resultado final
print("\nNúmeros presentes nas duas listas (sem repetição):", intersecao)
