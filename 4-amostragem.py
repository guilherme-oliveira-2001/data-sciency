# Amostragem Simples, Sistemática e Estratificada
import pandas as pd
import numpy as np
df= []

# Amostragem Simples
np.random.seed(12)
# Dentro dos parenteses pode ser usado qualquer número. Qualquer número inteiro indicado tem exclusivamente duas função no código: iniciliazar a gerador de números aleatórios e fixar a sequência geradam para que não seja gerada outra sequência ao rodar o comando novamente.

amostra = np.random.choice(a=[0,1], size = 150, replace=True, p=[0.7, 0.3])
# a=[0, 1] - Espaço amostral que será considerado pelo gerador de números.
# size=150 - Tamanho do vetor de númeoros gerados.
# replace=True - Se haverá reposição ou não, entre as opções do espaço amostral.
# p=[0.7, 0.3] - Probabilidade de cada número do espaço amostral ser escolhido, no caso, 70% de ser 0 a cada escolha e 30% de ser 1.

df.iloc[amostra==0]
# Nesse comando o iloc selecionará as linhas a partir da sequência aleatória gerada, associando os índices onde o valor for 0.

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Amostragem Sistemática
# Primeiro definir quantas amostras retirar da população.

base = list(range(150))
populacao = 150
amostra = 15
intervalo = int(populacao/amostra)

valor_max = populacao - (amostra - 1) * intervalo
inicio = np.random.randint(0, valor_max)

amostragem = []

for i in range(amostra):
    indice = inicio + i * intervalo
    amostragem.append(base[indice])

# Esse código gera utiliza alguns parâmetros para gerar uma amostragem de forma sistemática. Primeiro são inferidas a população e a quantidade de amostras desejadas e então, é calculado o intervalo, que define que a cada n valores, uma amostra é retirada da população. Mais dois parâmetros são calculados, que são: o "inicio" e o "valor_max". O início é um valor gerado aleatoriamente entre os índices 0 e 9 (10 não é considerado no range) que será o indice inicial dentro da base. Como o intervalo é de 10 amostras, a cada 10 amostras 1 é retirada. O looping do for é utilizado para percorrer o tamanho da variável amostra e coletar cada uma para adicionar na lista amostragem.

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Amostragem Estratificada
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
train_idx, test_idx = next(split.split(base, base['coluna']))
amostra_estratificada = base.loc[test_idx]
# n_splita=1 - Define quantas vezes a população será cortada. Neste caso, apenas uma.
# test_size=0.2 - Tamanho da amostragem. Esse método stratified gera duas divisões (treino e teste). Como iremos usar apenas uma das partes, opta-se por utilizar o test_size pois é parâmetro que é definido no método.
# random_state=42 - Qualquer número inteiro utilizado exclusivamente para fixar a escolha aleatória, pois, a cada vez que o algoritmo rodasse, uma nova fatia de amostras seria gerada.
# train_idx, test_idx - São as duas variáveis que devem armazenar o índice dos dados para treino e para teste, os quais foram fatiados da população estratificada. 
# next(split.split(variável, variável['coluna com as classes que serão estratificadas'])) - função do método que realiza de fato o fatiamento da população.
# base.loc[test_idx] - Atribuição das amostras estratificadas que foram fatiadas da população para dentro de uma variável.

# -------------------------------------------------------------------------------------------------------------------------------------------------

