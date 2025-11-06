tupla = [(2,4),(1,3),(7,10),(3,6)]


def Seleção(tupla):
    inicio,fim = tupla[0]
    for i in range(0,len(tupla)):
        a,b = tupla[i]
        if(a<fim):
            if(b>fim):
                fim = b
            if(a<inicio):
                inicio = a
                
    tuplaNova = [(inicio,fim),]
    
    for i in range(0,len(tupla)):
        a,b = tupla[i]
        if(a>fim):
            if(b<fim):
                tuplaNova.append((a,b))
            if(a>inicio):
                tuplaNova.append((a,b))
    return tuplaNova
            
            
tuplaNova = Seleção(tupla)            
            
print(tuplaNova)