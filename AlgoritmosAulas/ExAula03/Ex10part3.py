bit = input("insira 4 bits: ")
bit = int(bit)
a= bit//1000 #4321  4
b= (bit//100)%10    #4321 43 3
c = (bit//10)%10  #432 2
d = bit%10

print(a, b, c, d)

valor = (d*(2**0) + c*(2**1) + b*(2**2) + a*(2**3))
    
print("O valor dos bit é {}".format(valor))