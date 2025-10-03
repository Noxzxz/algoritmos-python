"""random()	Retorna um número de ponto flutuante aleatório no intervalo [0.0, 1.0).

randint(a, b)	Retorna um número inteiro aleatório entre a e b (inclusive ambos).

uniform(a, b)	Retorna um número de ponto flutuante aleatório entre a e b.

randrange(start, stop[, step])	Retorna um valor aleatório entre start e stop, com um intervalo opcional de step. Similar a range().

choice(seq)	Retorna um elemento aleatório de uma sequência (lista, tupla, string, etc.).

choices(population, weights=None, k=1)	Retorna uma lista com k elementos escolhidos aleatoriamente, com pesos opcionais. Permite repetições.

sample(population, k)	Retorna uma amostra com k elementos únicos da população (sem repetição).

shuffle(seq)	Embaralha a ordem dos elementos de uma sequência (modifica a lista original).

seed(a=None)	Inicializa o gerador de números aleatórios. Usado para garantir reprodutibilidade."""

import random

random.seed(42)  # define a semente
print(random.random())  # número entre 0.0 e 1.0
print(random.randint(1, 10))  # número inteiro entre 1 e 10
print(random.choice(['maçã', 'banana', 'laranja']))  # escolhe uma fruta
