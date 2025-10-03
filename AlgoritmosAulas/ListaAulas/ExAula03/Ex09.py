string = input('Insira um numero de 3 digitos: ')
a = [0,0,0]
k  = len(string)
for i in range (k):
    a[i] = string[(k - i - 1)]

print('O numero ivertido é {}'.format(a))