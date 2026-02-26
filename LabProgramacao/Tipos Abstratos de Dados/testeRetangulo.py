import random
from ponto import Ponto
from retangulo import Retangulo


lista = []
for _ in range(random.randint(1,10)):
    p = Ponto(random.randint(3,15), random.randint(4,16))
    altura = random.randint(5,10)
    largura = random.randint(3,12)
    lista.append(Retangulo(p,largura,altura))


for r in lista:
    centro = r.coordenada_centro()
    print(f"Área: {r.calcular_area()} |Perimetro: {r.calcular_perimetro()} | Coordenada do centro: X = {centro.x} Y = {centro.y}")
    