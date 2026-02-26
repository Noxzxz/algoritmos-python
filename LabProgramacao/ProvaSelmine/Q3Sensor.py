class Sensor:
    codigo: int
    leitura: int
    
    def __init__(self,codigo="", leitura=""):
        self.codigo = codigo
        self.leitura = leitura
        
    def __str__(self):
        return f"Codigo: {self.codigo} |Leitura: {self.leitura}"
    
        
def OrdenaSelecao(Lista):
    n = len(Lista)
    for i in range(n-1):
        menor = i
        for j in range(i+1,n):
            if Lista[j].leitura < Lista[menor].leitura:
                menor = j
        Lista[i], Lista[menor] = Lista[menor], Lista[i]
    return Lista
        
ListaSensor = []

ListaSensor.append(Sensor(10,112))
ListaSensor.append(Sensor(5,122))
ListaSensor.append(Sensor(9,12))
ListaSensor.append(Sensor(32,142))
ListaSensor.append(Sensor(33,13))

for i in ListaSensor:
    print(i)

ListaSensor = OrdenaSelecao(ListaSensor)

print("\n______________________________")
for i in ListaSensor:
    print(i)




    