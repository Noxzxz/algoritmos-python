leads = [
    {"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"},
    {"nome":"Beto","origem":"Google Ads","score":65,"status":"perdido"},
    {"nome":"Cris","origem":"Indicação","score":90,"status":"ganho"},
    {"nome":"Duda","origem":"Instagram","score":74,"status":"perdido"},
    {"nome":"Enzo","origem":"Google Ads","score":71,"status":"ganho"},
]

origem=[[],[],[]]

for i in (leads):
    if (i.get("origem") not in origem[0]):
        origem[0].append(i.get("origem"))
        origem[1].append(0)
        origem[2].append(0)
            
            
for j in range(len(origem[0])):
    for i in leads:    
        if(i.get("origem") == origem[0][j]):
            origem[1][j]+=1
            if(i.get("score")>=70 and i.get("status") == "ganho"):
                origem[2][j]+=1
                    
print(origem)              
                  
print("A taxa de conversão é") 
for i in range (len(origem)):
    print("Taxa de conversão  - ",origem[0][i],": ",origem[2][i]/origem[1][i])     