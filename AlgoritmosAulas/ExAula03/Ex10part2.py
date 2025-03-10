bit = input("Digite 4 bits ")
valor = 0

for i in range (4):
    if i==0 and int(bit[i]) == 1:
        valor+=1
    if i==1 and int(bit[i]) == 1:
        valor+=2
    if i==2 and int(bit[i]) == 1:
        valor+=4
    if i==3 and int(bit[i]) == 1:
        valor+=8

print("O valor é {}".format(valor))