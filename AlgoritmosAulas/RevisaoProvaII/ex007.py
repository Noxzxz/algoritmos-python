# Listas para armazenar os dados
nomes = []
vendas = []
pagamentos = []

# Entrada da quantidade de vendedores
qtd = int(input("Informe a quantidade de vendedores: "))

# Coleta dos dados
for i in range(qtd):
    print(f"\nVendedor {i+1}")
    nome = input("Nome: ")
    valor_vendas = float(input("Valor das vendas brutas: R$ "))

    nomes.append(nome)
    vendas.append(valor_vendas)

    # Cálculo do pagamento: R$200 fixo + 9% sobre as vendas
    pagamento = 200 + (0.09 * valor_vendas)
    pagamentos.append(pagamento)

# Saída dos resultados
print("\nRelatório de Pagamentos:\n")
for i in range(qtd):
    print(f"{nomes[i]} receberá R$ {pagamentos[i]:.2f}")
