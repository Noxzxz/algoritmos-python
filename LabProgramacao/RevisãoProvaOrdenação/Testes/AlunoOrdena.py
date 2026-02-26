class Aluno:
    nome: str
    RA: int
    nota1: float
    nota2: float

    def __init__(self, nome="", RA ="", nota1="",nota2=""):
        self.nome = nome
        self.RA = RA
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1+self.nota2)/2


def ordenarClass(lista):
    listaMaior = []
    usados = []
    tam = len(lista)

    for i in range(tam):
        maior = i
        for j in range(tam):
            if j in usados:
                continue
            if(lista[maior].media()<lista[j].media()):
                maior = j

        listaMaior.append(lista[maior])
        usados.append(maior)

    return listaMaior

"""
SEM criar outra lista, ordenação da propria tabela
def ordenarClass(lista):
    tam = len(lista)

    for i in range(tam):
        maior = i

        for j in range(i + 1, tam):
            if lista[j].media() > lista[maior].media():
                maior = j

        lista[i], lista[maior] = lista[maior], lista[i]

    return lista    
"""


ListaAluno = [
    Aluno("Ihan",1,10,10),
    Aluno("Ihago",1,9,10),
    Aluno("Evelyn",1,7,8),
    Aluno("Rodrigo",1,1,3),
    Aluno("Icaro",1,10,8)
]

ListaAluno = ordenarClass(ListaAluno)

for i in ListaAluno:
    print(f"Nome: {i.nome} |Media:{i.media()}")