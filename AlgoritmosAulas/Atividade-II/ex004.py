<<<<<<< HEAD
varGlob = 400000
termPar = 0
fib = 1
aux=0
vetsomaPar= []
while fib < varGlob and aux < varGlob:
    print(fib)
    aux, fib = fib, fib+aux
    
    if(fib%2==0):
        vetsomaPar.append(fib)
    

somarPar = 0
for i in (vetsomaPar):
    somarPar+= i
print("A soma dos valores pares é {}".format(somarPar))
=======
varGlob = 10
termPar = 0
fib = 1
aux=0
for i in range(varGlob):
    print(fib)
    aux, fib = fib, fib+aux
>>>>>>> f297a1c55904f9cd12503ff208d339c0671281fa
        