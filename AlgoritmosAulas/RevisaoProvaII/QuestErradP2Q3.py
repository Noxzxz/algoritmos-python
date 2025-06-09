opcoes = [
    "Windows Server",
    "Unix",
    "Linux",
    "Netware",
    "Mac OS",
    "Outro"
]

votos = [0] * 6  # Lista para contar os votos de cada sistema

print("Digite os votos (1 a 6). Digite 0 para encerrar.")

while True:
    try:
        voto = int(input("Voto (1-6 ou 0 para encerrar): "))
        if voto == 0:
            break
        elif 1 <= voto <= 6:
            votos[voto - 1] += 1
        else:
            print("Valor inválido! Digite um número entre 1 e 6.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

# Cálculo do total de votos
total_votos = sum(votos)

# Impressão do cabeçalho da tabela
print("\nSistema Operacional    Votos   %")
print("-------------------    -----   ----")

for i in range(len(opcoes)):
    if total_votos > 0:
        percentual = (votos[i] / total_votos) * 100
    else:
        percentual = 0
    print(f"{opcoes[i]:<21} {votos[i]:<7} {percentual:.2f}%")

print("-------------------    -----")
print(f"Total                  {total_votos}\n")

# Verifica o(s) vencedor(es)
maior_voto = max(votos)
indices_vencedores = [i for i, v in enumerate(votos) if v == maior_voto]

if len(indices_vencedores) == 1:
    idx = indices_vencedores[0]
    percentual = (votos[idx] / total_votos) * 100
    print(f"O Sistema Operacional mais votado foi o {opcoes[idx]}, com {votos[idx]} votos, correspondendo a {percentual:.2f}% dos votos.")
elif len(indices_vencedores) == 2:
    idx1, idx2 = indices_vencedores
    percentual = (votos[idx1] / total_votos) * 100
    print(f"Houve um empate entre {opcoes[idx1]} e {opcoes[idx2]}, com {maior_voto} votos cada, correspondendo a {percentual:.2f}% dos votos.")
else:
    print("Houve um empate entre mais de dois sistemas, o que não é previsto na regra.")
