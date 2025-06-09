a = int(input("Insira o valor do lado A:"))
b = int(input("Insira o valor do lado B:"))
c = int(input("Insira o valor do lado C:"))

if(a+b>c and a+c>b and b+c>a):
    if(a**2==b**2+c**2):
        print("É um triangulo retangulo")
    
    elif(a**2>b**2+c**2):
        print("É um triangulo obtusangulo")
    
    elif(a**2<b**2+c**2):
        print("É um triangulo acutangulo")
else:
    print("Não é um triangulo")