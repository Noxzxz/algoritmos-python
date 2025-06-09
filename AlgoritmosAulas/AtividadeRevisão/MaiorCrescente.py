a = input("Insira o 1° numero: ")
b = input("Insira o 2° numero: ")
c = input("Insira o 3° numero: ")

if(c>b>a):
    a,b,c = c,b,a
elif(b>c>a):
    a,b,c = b,c,a
elif(a>c>b):
    a,b,c = a,c,b
print(c+" "+b+" "+a)
