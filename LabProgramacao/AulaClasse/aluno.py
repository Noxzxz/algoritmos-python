class Aluno:
    #atributos (variaveis de instancia) do objeto --> propriedades
    nome :str
    ra: int
    nota1: float
    nota2: float
    
    #construtor
    def __init__(self, nome ="", ra = 0, nota1 = 0, nota2 =0):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self) -> float:
        return(self.nota1 + self.nota2)/2

    def situacao(self) ->str:
        media = self.calcular_media()
        if media >= 7.0:
            return "APROVADO"
        return "REPROVADO"
    
    def impress(self):
        return f"Nome: {self.nome}, Ra: {self.ra}, Nota 1: {self.nota1}, Nota 2: {self.nota2}, Media: {self.calcular_media()}"