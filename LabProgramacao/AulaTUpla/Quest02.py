TuplaP1 = [
    ("Ana", 7.5), ("Bruno", 8.0), ("Carla", 6.5), ("Daniel", 9.0), ("Eduarda", 5.5),
    ("Felipe", 8.2),("Gabriela", 7.0), ("Heitor", 6.0), ("Isabela", 9.5), ("João", 7.8)]

TuplaP2 = [ 
    ("Ana", 8.0), ("Bruno", 7.0), ("Carla", 7.5), ("Daniel", 9.2), ("Eduarda", 6.0),
    ("Felipe", 8.8), ("Gabriela", 7.4), ("Heitor", 6.5), ("Isabela", 9.8), ("João", 8.5)
]

def CriarTuplaAd(tupla1, tupla2):
    TuplaFusion = tuple((tupla2[i][0],tupla1[i][1],tupla2[i][1]) for i in range(len(tupla1)))
    return TuplaFusion

def melhoriaAluno(tuplaComp):
    listMelhoria = []
    for i in range(len(tuplaComp)):
        if tuplaComp[i][1]<tuplaComp[i][2]:
            listMelhoria.append(tuplaComp[i][0])
    return listMelhoria

def QuedaAluno(tuplaComp):
    listQueda = []
    for i in range(len(tuplaComp)):
        if tuplaComp[i][1]>tuplaComp[i][2]:
            listQueda.append(tuplaComp[i][0])
    return listQueda

def manterAluno(tuplaComp):
    listManter = []
    for i in range(len(tuplaComp)):
        if tuplaComp[i][1]==tuplaComp[i][2]:
            listManter.append(tuplaComp[i][0])
    return listManter


TuplaFusion = CriarTuplaAd(TuplaP1,TuplaP2)
listMelhoria = melhoriaAluno(TuplaFusion)
listQueda = QuedaAluno(TuplaFusion)
listManter = manterAluno(TuplaFusion)

print(TuplaFusion,"\n")

print(f"Os alunos que tiveram um aumento do desempenho: \n",listMelhoria)
print(f"Os alunos que mantivera o mesmo desempenho: \n",listManter)
print(f"Os alunos que tiveram uma queda no desempenho: \n",listQueda)

