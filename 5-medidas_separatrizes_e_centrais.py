# Medidas de tendencia central, separatrizes e de dispersão
from scipy import stats
import numpy as np

np.mean()
np.median()
stats.mode()

np.quantile([0, 0.25, 0.5, 0.75, 1])

np.std(ddof=1)
np.var(ddof=1) 
# ddof=1 - Quando o desvio padrão e variância são utilizados na população, ddof=0. Quando utilizados em amostra, ddof=1. Esse parâmetro igual a 1 é para compensar o viés que pode ocorrer na amostra.
# Dentro do parenteses deve-se indicar os dados que serão trabalhados.