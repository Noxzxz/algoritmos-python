'''
A partir de uma lista de palavras (pode haver repetição), imprimir a quantidade de vezes que cada palavra aparece.
'''

listaPav = ['Gato','Sol','Mar','Flor','Gato','Sol','Lua','Flor']
listaEsc = {}

for palavra in listaPav:
    if palavra not in listaEsc:
        listaEsc[palavra] = 0
    listaEsc[palavra] += 1

for palavra, valor in listaEsc.items():
    print(f'{palavra}: {valor}')
    
    
listaVogais = {}

vogais = ['a','e','i','o','u']

for palavra in listaEsc:
    cont = 0
    for letra in palavra:    
        if letra in vogais:
            cont += 1
    listaVogais[palavra] = cont  

        
for chave, valor in listaVogais.items():
    print(f"{chave} --> {valor}")