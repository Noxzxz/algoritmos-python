a = int(input("Insira o valor do 1° lado: "))
b = int(input("Insira o valor do 2° lado: "))
c = int(input("Insira o valor do 3° lado: "))

if(a<b+c and b<a+c and c<a+c):
    print("Esses valores representam os lados de um triângulo")
else:
    print("Não é um triangulo")
    