fat = int(input("Insira um valor"))

fatorialResult = fat
while (fat>1):
    fat= fat - 1
    fatorialResult = fat * fatorialResult 
    print(fatorialResult)
    
    
print("O fatorial é {}".format(fatorialResult))