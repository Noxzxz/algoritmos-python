def rotacionar(a,b):
    frase = ""
    for i in a:
        if(ord(i)==32):
            aux= ord(i)
        elif(ord(i)+b>122):
            aux = (ord(i)+b)-26
        else:
            aux = ord(i)+b
        frase = frase+ chr(aux)
    return frase

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

print(rotacionar(a,b))

