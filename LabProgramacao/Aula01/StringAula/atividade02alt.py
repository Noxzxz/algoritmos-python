def desrotacionar(a,b):
    frase = ""
    for i in a:
        if(ord(i)==32):
            aux= ord(i)
        elif(ord(i)-b>97):
            aux = (ord(i)-b)+26
        else:
            aux = ord(i)-b
        frase = frase+ chr(aux)
    return frase


a = input("Informe uma frase: ").lower()
b = int(input("Insira um numero: "))

frase = desrotacionar(a,b)
print(frase)