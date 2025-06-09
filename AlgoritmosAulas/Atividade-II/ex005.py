a = input("Insira um numero binario: ")
numD = 0


for i in range(len(a)):
    numD += int(a[-(i+1)]) * (2**i)
print("O numero em decimal é {}".format(numD))
