leads = [
    {"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"},
    {"nome":"Beto","origem":"Google Ads","score":65,"status":"perdido"},
    {"nome":"Cris","origem":"Indicação","score":90,"status":"ganho"},
    {"nome":"Duda","origem":"Instagram","score":74,"status":"perdido"},
    {"nome":"Enzo","origem":"Google Ads","score":71,"status":"ganho"},
]


dic = {}

for i in leads:
    origem = i.get("origem")
    if origem not in dic:
        dic[origem] = {"Total": 0, "Ganhos": 0, "Conversão": 0}

    dic[origem]["Total"]+=1

    if i.get("score")>=70 and i.get("status")=="ganho":
        dic[origem]["Ganhos"]+=1

for i in dic:
    dic[i]["Conversão"] = (dic[i]["Ganhos"])/(dic[i]["Total"])


print(dic)
 