import pandas as pd
import numpy as np
from minisom import MiniSom
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Passo 1: Ler o arquivo Excel
dados = pd.read_excel('C:/Users/ihan.nunes/AlgoritmosAulas/EstudoSOM/SuperstoreSalesBrasil.xls')

# Passo 2: Converter para matriz NumPy
matriz_dados = dados.to_numpy()

# Passo 3: Normalizar os dados
scaler = MinMaxScaler()
matriz_normalizada = scaler.fit_transform(matriz_dados)

# Passo 4: Inicializar o SOM
# Ajustando para o número de dimensões da matriz (matriz_normalizada.shape[1])
som = MiniSom(10, 10, matriz_normalizada.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(matriz_normalizada)

# Passo 5: Treinar o SOM
som.train_random(matriz_normalizada, 500)  # Ajuste o número de iterações conforme necessário

# Passo 6: Mapear os dados
for i, dado in enumerate(matriz_normalizada):
    vencedor = som.winner(dado)  # Coordenadas do BMU (neurônio vencedor)
    print(f'Dado {i} mapeado no neurônio {vencedor}')
    
    
    
#codigo copilot 
import pandas as pd

resultados = pd.DataFrame({
    'Dados': [f'Dado {i}' for i in range(len(matriz_normalizada))],
    'Neurônio Vencedor': [som.winner(dado) for dado in matriz_normalizada]
})

print(resultados.head())  # Mostra os primeiros resultados

'''
import numpy as np

# Criar uma matriz para contar pontos por neurônio
mapa = np.zeros((10, 10))

for dado in matriz_normalizada:
    vencedor = som.winner(dado)
    mapa[vencedor[0], vencedor[1]] += 1

# Visualizar com um mapa de calor
plt.imshow(mapa, cmap='cool', interpolation='nearest')
plt.colorbar(label='Número de Dados')
plt.title("Mapa de Densidade dos Neurônios")
plt.xlabel("X dos Neurônios")
plt.ylabel("Y dos Neurônios")
plt.show()

 Aplicar K-means nos pesos do SOM
import matplotlib.pyplot as plt

# Configurar gráfico
plt.figure(figsize=(10, 10))

# Plotar os pontos baseados nos neurônios vencedores
for i, dado in enumerate(matriz_normalizada):
    vencedor = som.winner(dado)
    plt.plot(vencedor[0] + 0.5, vencedor[1] + 0.5, 'o', markersize=5, label=f'Dado {i}' if i < 10 else None)

plt.xlim(-0.5, 10.5)
plt.ylim(-0.5, 10.5)
plt.title("Visualização dos Neurônios Vencedores")
plt.xlabel("X dos Neurônios")
plt.ylabel("Y dos Neurônios")
plt.grid(True)
plt.legend(loc='best', fontsize='small')
plt.show()'''