
#bloco de leitura de arquivo
with open("alunos.txt", "r") as arquivo:
    cont= 0
    for linha in arquivo:
        linha = linha.strip()
        nome, nota1,nota2 = linha.split(";")
        media = (float(nota1)+float(nota2))/2
        print(f"{nome} --> {media:.2f}")
        if media>=7:
            print("APROVADO!!")
            cont+=1
        
print("A quantidade de aprovado é ",format(cont))
        
        