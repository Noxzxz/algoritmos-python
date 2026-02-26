class Livro: 
    id: int
    titulo: str
    autor: str
    ano: int
    
    def __init__(self, id ="", titulo ="", autor="", ano=""):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        
    def __str__(self):
        return f"Id: {self.id} | Titulo: {self.titulo}\nAutor: {self.autor} |Ano: {self.ano}"
        

def ordena(Lista):
    tam = len(Lista)
    for i in range(tam):
        maior = i
        for j in range(i, tam):
            if Lista[j].id< Lista[maior].id:
                maior = j
        Lista[i], Lista[maior] = Lista[maior], Lista[i]
    return Lista

#eSei que tem que retornar false ou true, mas eu queria deixar bonito
def busca_binaria(lista, valor):
    ini, fim = 0, len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio].id == valor:
            return meio #só colcoar True no lugar
        elif lista[meio].id < valor:
            ini = meio + 1
        else:
            fim = meio - 1
    return False

#ApresentaçãoBonitaaa
def ApresentBonita(lista,valor):
    #Busca binaria  
    posic = busca_binaria(lista,valor)    
    if(posic!= False):
        return lista[posic]
    else:
        return f"{posic}, id não encontrado"
    
    
def MinMax(lista, inicio, fim):
    listaAno = []
    for i in range(len(lista)):
        if lista[i].ano>=inicio and lista[i].ano<=fim:
            listaAno.append(lista[i])
    return listaAno


Listaaaaaa = []

Listaaaaaa.append(Livro(5,"Cronicas de Faerun", "Palp",2025))
Listaaaaaa.append(Livro(1,"SouthWold: V5", "Jimmi",2024))
Listaaaaaa.append(Livro(3,"Warsaw by Nigth", "Loan",2023))
Listaaaaaa.append(Livro(7,"Transilvania By night", "Loan",2023))
Listaaaaaa.append(Livro(10,"Não existe amor em SP", "Rock",2021))
     
#Teste Ordenação     
for i in Listaaaaaa:
    print(i) 
        
print("\n_____________________________________________________") 
Listaaaaaa = ordena(Listaaaaaa)

for i in Listaaaaaa:
    print(i)
  
print("\n_____________________________________________________")
#Busca binaria  
print(ApresentBonita(Listaaaaaa,8))
    
print("\n_____________________________________________________")    


#Entre x e y
x,y= 2021,2023
listaIntervalo = MinMax(Listaaaaaa,x,y)
print(f"Livros no intervalo de {x} e {y}")
for i in listaIntervalo:
    print(i,"\n______________")
    
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
num = int(input("Insira o numero de livros: "))
listaLivro = []
for i in range(num):
    id = int(input("Insira o id do livro: "))
    NomeL =  input("Insira o nome do livro: ")
    NomeAut = input("Insira o nome do autor: ")
    Ano = int(input("Insira o ano do livro: "))
    print("\n")
    
    listaLivro.append(Livro(id,NomeL,NomeAut,Ano))

#Ordenaçãooo
listaLivro = ordena(listaLivro)
for i in listaLivro:
    print(i,"\n________")
    
#Buscaaaa
posic = int(input("Insira o id do livro buscado"))
print(ApresentBonita(listaLivro,posic))

#Intervaloooo
x = int(input("\nInsira valor do inicio do intervalo: "))
y = int(input("Insira valor do fim do intervalo: "))

listaIntervalo = MinMax(listaLivro,x,y)

print(f"\nLivros no intervalo de {x} e {y}")
for i in listaIntervalo:
    print(i,"\n______________")
