import random

def geraPontos(n):
    listaTransi = []
    for i in range (n):
        listaTransi.append([(random.randint(1,10)),(random.randint(1,10))])
    tuplaCoordenada = (*listaTransi,)
    return tuplaCoordenada

#RESPOSTA A
def MaiorPontos(tuplaAlvo):
    for i in range(len(tuplaAlvo)):
        if i==0:
            DistX, DistY = tuplaAlvo[0]
        trans1,trans2 = tuplaAlvo[i]
        if(((DistX**2)+(DistY**2))**(1/2)<((trans1**2)+(trans2**2))**(1/2)):
            DistX, DistY = tuplaAlvo[i]
    return DistX, DistY

#RESPOSTA B
def MenorPontos(tuplaAlvo):
    for i in range(len(tuplaAlvo)):
        if i==0:
            DistX, DistY = tuplaAlvo[0]
        trans1,trans2 = tuplaAlvo[i]
        if(((DistX**2)+(DistY**2))**(1/2)>((trans1**2)+(trans2**2))**(1/2)):
            DistX, DistY = tuplaAlvo[i]
    return DistX,DistY

#RESPOSTA C
def Media(tuplaAlvo):
    media = 0
    for i in range(len(tuplaAlvo)):
        trans1,trans2 = tuplaAlvo[i]
        media += ((trans1**2)+(trans2**2))**(1/2)
    media = media/len(tuplaAlvo)
    return media


def main():
    tuplaCoordenada = geraPontos(5)

    distMaior = MaiorPontos(tuplaCoordenada)
    distMenor = MenorPontos(tuplaCoordenada)
    MediaDist = Media(tuplaCoordenada)

    print(tuplaCoordenada)
    print(f"O valor mais distante da origem é {distMaior}")
    print(f"O valor mais proximo da origem é {distMenor}")
    print(f"O valor medio de distancia é {MediaDist:.2f}")


if __name__ == "__main__":
    main()