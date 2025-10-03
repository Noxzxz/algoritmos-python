print(5/5,8%5,8//5)
n = int(input("Insira o valor: "))

selo3, selo5,resto= 0,0,0
if(n//3>=1 and ((n%3)%5 == 0 or n%3 == 0)):
    selo3+= n//3
    n -= n//3*3
if(n//5>=1 and ((n%5)%3 == 0 or n%5 == 0)):
    selo5+= n//5
    n -= n//5*5
if(n//3>=1):
    selo3+= n//3
    n -= n//3*3
if(n!= 0 ):
    resto = n
    
print(f"O numero de selos necessario é\nselos 3: {selo3}\nselos 5: {selo5}\nresto: {resto} and {n}")