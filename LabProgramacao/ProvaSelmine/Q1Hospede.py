class Hospede:
    Nome: str
    
    def __init__(self, Nome = ""):
        self.Nome = Nome
        
class Quarto:
    NumQuart: int
    ValDia: float
    
    def __init__(self, NumQuart = "", ValDia = ""):
        self.NumQuart = NumQuart
        self.ValDia = ValDia
        
class Reserva:
    Hospede: Hospede
    Quarto: Quarto
    TotalDias: int
    
    def __init__(self, Hospede = Hospede(""), Quarto = Quarto("",""), TotalDias =""):
        self.Hospede = Hospede
        self.Quarto = Quarto
        self.TotalDias = TotalDias
        
    def ValorTotal(self):
        return self.TotalDias*self.Quarto.ValDia
    
    def __str__(self):
        return f"Nome Hospede: {self.Hospede.Nome} | Numero do Quarto: {self.Quarto.NumQuart} | Valor diaria: {self.Quarto.ValDia}\nTotal de dias: {self.TotalDias} | Valor Total: {self.ValorTotal():.2f}"        
    
def ImpressLista(Lista):
    for i in Lista:
        print(i,"\n")
        
def ImpressTotDia(Lista):
    Tot = 0
    for i in Lista:
        Tot+= i.ValorTotal()
    return Tot

def BuscaNm(Lista, Nm):
    for i in Lista:
        if i.Hospede.Nome == Nm:
            return (f"{i.Hospede.Nome}: R$ {i.ValorTotal()}")
    
#Codigo Brutal Moggador

n = int(input("Insira o numero de hospedes para cadastro: "))

listaReservas, listaHospede, listaQuarto = [], [], []

for i in range(n):
    Nm = input("Insira o nome do Hospede: ")
    NumQ = int(input("Insira o numero do quarto: "))
    ValDiaria = float(input("Insira o valor da diaria: "))
    TotDias = int(input("Insira o numero de diarias: "))
    listaReservas.append(Reserva(Hospede(Nm),Quarto(NumQ,ValDiaria),TotDias))
    listaHospede.append(Hospede(Nm))
    listaQuarto.append(Quarto(NumQ,ValDiaria))
    print("")
    
print("________________________________________________\n")
    
print(ImpressLista(listaReservas))

print("________________________________________________\n")

print("O valor total que a pousada recebera com as reservas é: ",ImpressTotDia(listaReservas))

print("________________________________________________\n")

print(BuscaNm(listaReservas, "ihan"))



