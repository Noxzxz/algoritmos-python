'''
Programa exemplo para ler o RA, o nome e a nota dos alunos matriculados
na disciplina Felicidade. Em seguida imprimir a quantidade de alunos com media(maior ou igual a 7) 
'''

lista= []

for i in range(1):
    ra = int(input("RA: "))
    nome = input("Nome: ")
    nota = float(input("Media Nota: "))
    lista.append({'ra':ra,'nome':nome,'nota':nota})
    print("")
    
#quantidade de alunos que estão com notas acima da media
tot =0
for i in range(len(lista)):
    aluno = lista[i]
    if aluno.get('nota')>= 7.0:
        tot+=1    
    print("Alunos com nota 7 ou acima: ",tot)

print(lista)