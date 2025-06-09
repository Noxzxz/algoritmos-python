a = int(input("Insira um numero qualquer: "))

i=0
while(a>0):
    a = a//10
    i+=1
    
print("O numero inserido tem {}° casa(s) decimal(is)".format(i))