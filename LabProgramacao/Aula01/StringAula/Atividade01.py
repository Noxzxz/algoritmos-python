n =  int(input(""))

for i in range (n):
    a = input("")
    frase = ""
    for i in a:
        if i.isalpha():
            frase += chr(ord(i)+3)
        else:
            frase += i

    frase = str(frase[::-1])
    novafrase = ""

    num = int(len(a)/2)
    for i in range (len(a)):
        if(i>=int(num)):
            novafrase += chr(ord(frase[i])-1)
        else:
            novafrase += frase[i]
    print(novafrase)