from ponto import Ponto

lista = []
quantidade = int(input("Qual a quantidade de pontos?  "))
for _ in range(quantidade):
    x = int(input("Coordenada x: "))
    y = int(input("Coordenada y:"))
    lista.append(Ponto(x, y))
    
#impressão de cada ponto e sua respectiva distância até o centro (0,0)
print("Distancia de cada ponto até a orifem (0,0): ")
for pontos in lista:
    print(f"{pontos} -> {pontos.calcular_distancia_ate_origem():.2f}")
