# Distribuição Normal (Gaussiana)

# A distribuição nornal ou gaussiana é utilizada amplamente em calculos probabilisticos, onde um conjunto de dados discretos dispostos em intervalos de desvios padrão são referenciados para estimar a probabilidade de um evento acontecer. É semelhante a um sino devido a distribuição normal ser simétrica.

from scipy.stats import norm

norm.cdf(6, 8, 2)
# a função cdf do método norm, que representa a distribuição normal, serve para calcular a probabilidade de um evento ser menor que determinado intervalo
# A função vai calcular a probabilidade de um evento ser menor que 6, onde 8 é a media do conjunto e o 2 o desvio padrão.

norm.sf(10, 8, 2)
# a função sf é o inverso, servindo para calcular a probabilidade de um evento ser maior do que  que determinado intervalo
# A função vai calcular a probabilidade de um evento ser maior que 10, onde 8 é a media do conjunto e o 2 o desvio padrão.

