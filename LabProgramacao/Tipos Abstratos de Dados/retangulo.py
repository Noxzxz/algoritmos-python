import math
from ponto import Ponto

class Retangulo:
    canto_superior_esquerdo : Ponto
    altura = float
    largura = float
    
    def __init__(self, canto_superior_esquerdo: Ponto, altura = 0, largura = 0):
        self.canto_superior_esquerdo = canto_superior_esquerdo
        self.altura = altura 
        self.largura = largura 

    def calcular_area(self)-> float:
        return self.altura*self.largura

    def calcular_perimetro(self)->float:
        return 2* (self.altura + self.largura)

    def aumentar_tamanho(self, altura:float, largura:float)->float:
        self.largura+= largura
        self.altura += altura
    
    def coordenada_centro(self)-> Ponto:
        xc = self.canto_superior_esquerdo.x + self.largura/2
        yc = self.canto_superior_esquerdo.y + self.altura/2
        return Ponto(xc,yc)


"""
listaRetang = []

for i in range (3):
    listaRetang += Retangulo(i,i+2)

print(listaRetang)
print(listaRetang[0].)"""