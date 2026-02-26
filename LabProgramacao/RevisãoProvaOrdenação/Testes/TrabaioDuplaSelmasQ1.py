class Emprestimo:
    ValorFinanciado: float
    TaxaJurosM: float
    NumParcel: int
    IdentiEmp: str
    NmClie: str

    def __init__(self, ValorFinanciado ="", taxaJurosM = "", NumParcel= "", IdentiEmp ="", NmClie =""):
        self.ValorFinanciado = ValorFinanciado
        self.TaxaJurosM = taxaJurosM
        self.NumParcel = NumParcel
        self.IdentiEmp = IdentiEmp
        self.NmClie = NmClie

    def Parcelfixa(self):
        if self.TaxaJurosM == 0:
            return (self.ValorFinanciado/self.NumParcel)
        if self.TaxaJurosM > 0:
            return (self.ValorFinanciado*(self.TaxaJurosM/(1-(1+self.TaxaJurosM)**(-self.NumParcel))))
        
    def SaldoDev(self):
        if self.NumParcel>=12:
            return self.ValorFinanciado*(1+self.TaxaJurosM)**12 - self.Parcelfixa()*(((1+self.TaxaJurosM)**12-1)/self.TaxaJurosM)
        return 0
    
    def TotJuros(self):
        return self.NumParcel*self.Parcelfixa() - self.ValorFinanciado
    
    def CustTot(self):
        return self.NumParcel*self.Parcelfixa()
    
    def __str__(self):
        return f"Valor Financiado: {self.ValorFinanciado}| Taxa de Juros: {self.TaxaJurosM*100}%| Numero de Parcelas: {self.NumParcel}\nIdentificado Emprestimo: {self.IdentiEmp}| Nome Cliente: {self.NmClie}"
    
    def Listagem1(self):
        return f"Identificado Emprestimo: {self.IdentiEmp}| Parcela: {self.Parcelfixa():.2f}| Juros Totais: {self.TotJuros():.2f}| Custo Total: {self.CustTot():.2f}"
    
    def Listagem2(self):
        return f"Identificador Emprestimo: {self.IdentiEmp}| Saldo Devedor: {self.SaldoDev():.2f}"

"""
k = Emprestimo(10000,0.05,10,"Plano - Endividamento","ihago")

print(k)
print(k.Listagem1())
print(k.Listagem2())
""" 

num = int(input("Insira o numero de Operações bancarias: "))
listaEmp = []
for i in range(num):
    ValT = float(input("Insira o valor do emprestimo: "))
    taxJ = float(input("Insira o valor da taxa de juros(Ex: 0.05): "))
    NumP = int(input("Insira o numero de parcelas do emprestimo: "))
    IdEmp = input("Insira o identificador do emprestimo: ")
    NmClie = input("Insira o nome do cliente: ")
    listaEmp.append(Emprestimo(ValT,taxJ,NumP,IdEmp,NmClie))

print("_____________________________________________--")
for i in listaEmp:
    print(i)
    print(i.Listagem1())
    print(i.Listagem2())
