from math import sqrt
class Ponto:
    x : int
    y : int
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def calcular_cords(self) -> float:
        return (sqrt((self.x) ** 2) + (self.y)** 2)
        