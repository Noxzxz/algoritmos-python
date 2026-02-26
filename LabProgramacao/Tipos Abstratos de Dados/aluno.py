#chamada de construtor, pois está construindo um objeto do tipo Aluno
class Aluno:
    #atributos (variavel de instancia) do objeto --> propriedades
    nome : str
    ra : int
    nota1: float
    nota2: float
    
    #construtor
    #a função do atributo é receber valores iniciais para os atributos do objeto
    def __init__(self, nome = '', ra = 0, nota1 = 0, nota2 = 2):
        #para indicar que voce está atribuido valor a variavel do objeto utilizamos o self
        #utilizar o self apenas dentro da classe
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        
    #não precisa de parametro pois já está dentro do objeto
    #metodo para calcular e retorna a média simple
    def calcula_media(self) -> float:
        return (self.nota1 + self.nota2)/2
    
    #método para retornar a situação do aluno (aprovado ou reprovado)
    #precisa do self pois precisamos do método calcula média que está dentro de um objeto
    def situacao(self) -> str:
        media = self.calcula_media()
        if media >= 7.0:
            return 'APROVADO'
        return 'REPROVADO'
    
    
    