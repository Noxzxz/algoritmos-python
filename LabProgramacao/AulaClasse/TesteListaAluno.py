from AulaClasse.aluno import Aluno

a = Aluno("Selmini",2,10,9)
b = Aluno("Surian",1,8,9)
c = Aluno("Surjam")
d = Aluno("Sandra",4,9,9)
e = Aluno("Seblrer",5)
f = Aluno("Safa",6,2)
g = Aluno("Sinci Vader",0,1,9)

listaAl = []
listaAl.append(a)
listaAl.append(b)
listaAl.append(c)
listaAl.append(d)
listaAl.append(e)
listaAl.append(f)
listaAl.append(g)

print(listaAl[1].impress())

for i in  (listaAl):
    print(i.impress(),"\n",i.situacao(),"\n-----------------------")
    
    
listaInput = []    
for i in range(2):
    nome = input("Nome: ")
    Ra = int(input("RA: "))
    Nota1 = float(input("Nota 1:"))
    Nota2 = float(input("Nota 2:"))
    listaInput.append(Aluno(nome,Ra,Nota1,Nota2))
    
for i in range (len(listaInput)):
    print(listaInput[i].impress(),"\n",listaInput[i].situacao(),"\n-----------------------")