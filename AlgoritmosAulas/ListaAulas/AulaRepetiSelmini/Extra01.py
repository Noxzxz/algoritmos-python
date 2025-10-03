bin = input("Insira um numero binario: ")

len = len(bin)

bin = int(bin)
print(bin//10, bin%10)   
i=1
val=0
while(i <= len):
    if(i>1):
        val += (bin%10)*(2**(i-1))
    else:
        val += (bin%10)
    bin = bin//10
    i+=1
    
print(val)