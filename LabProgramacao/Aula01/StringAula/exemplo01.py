a = input("Informe uma palavra: ").lower()
for a in a:
    print(f"Letra = {a}| código = {ord(a)}")

lista = [4,5,6,97,124]
for i in lista:
    print(chr(i))