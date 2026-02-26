from aluno import Aluno

#sem essa função não acontece a geração da variavel a, representa um objeto, cujo o tipo é uma classe
#0x -> significa hexadecimal 16 numeros 
#ele vai de 0 a 9 e o 11 ao 15 representa as letras de A a F
#então 0x7ffde5c3d0d0 é um endereço de memória onde o objeto está armazenado
#chamda de variavel de referência  
a = Aluno('selmini', 44, 5, 7)
b = Aluno()

print(a)
print(a.nome)
print(b.nome)
media = a.calcula_media()
print(media)

#calcular ()   função
#x.calcular()  método

#fazer uma lista de alunos
lista = []
#temos 3 objetos pois o for gera um objeto a cada posição
for _ in range(3):
    nome = input("Nome -->  ")
    ra = int(input("RA -->  "))
    nota1 = float(input("Nota 1 -->  "))
    nota2 = float(input("Nota 2 -->  "))
    #sempre chamar o construtor antes: Aluno
    lista.append(Aluno(nome, ra, nota1, nota2))
    print('_' * 30)
    
   
#IMPRESSÃO 
#impressão do nome, da média e da situação
print(f"{'nome':<20}{'média':<10}{'Situação'}")#coluna com espaçamento de 20 caracteres (se não entrar nenhum valor, ela fica vazia)
#linha pontilhada
print('-' * 40)
#ainda estamos fazendo a impressão
for alunos in lista:
    media = alunos.calcular_media()
    print(f"{alunos.nome:<20}{media:<10.2f}{alunos.situacao()}")