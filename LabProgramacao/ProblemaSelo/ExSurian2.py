print(5/5,8%5,8//5)
n = int(input("Insira o valor: "))

selo3, selo5,resto= 0,0,n
if(n//3>=1):
    selo3+= n//3
    resto -= resto//3*3
    if(resto!= 0 and ((selo3*3)//5>=1)):
        selo5+= (n+(selo3*3))//5
        selo3-= ()
if(n!= 0 ):
    resto = n
    
print(f"O numero de selos necessario é\nselos 3: {selo3}\nselos 5: {selo5}\nresto: {resto} and {n}")