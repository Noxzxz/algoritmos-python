# Listas para armazenar os dados
nomes = []
precos_custo = []
precos_venda = []

# Leitura da quantidade de produtos
quantidade = int(input("Quantos produtos deseja cadastrar? "))

# Coleta dos dados de cada produto
for i in range(quantidade):
    print(f"\nProduto {i + 1}")
    nome = input("Nome do produto: ")
    custo = float(input("Preço de custo: "))
    venda = float(input("Preço de venda: "))
    
    nomes.append(nome)
    precos_custo.append(custo)
    precos_venda.append(venda)

# Listas de acordo com a faixa de lucro
lucro_10_30 = []
lucro_maior_30 = []

# Processa os dados
for i in range(quantidade):
    custo = precos_custo[i]
    venda = precos_venda[i]
    lucro_percentual = ((venda - custo) / custo) * 100

    if 10 <= lucro_percentual <= 30:
        lucro_10_30.append(nomes[i])
    elif lucro_percentual > 30:
        lucro_maior_30.append(nomes[i])

print("\nProdutos com lucro entre 10% e 30%:")
for nome in lucro_10_30:
    print("-", nome)

print("\nProdutos com lucro maior que 30%:")
for nome in lucro_maior_30:
    print("-", nome)
