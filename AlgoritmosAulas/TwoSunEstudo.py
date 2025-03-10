def twoSUn(tabela, target):
    for i in range(len(tabela)):
        for temp in range(i+1,len(tabela)):
            if(tabela[i] + tabela[temp] == target):
                return(i, temp)
            
print(twoSUn([1,1,2,3,4],5))