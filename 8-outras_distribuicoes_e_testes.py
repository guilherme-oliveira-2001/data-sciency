# Distribuição T de Student / Distribuição Binomial / Teste Qui-Quadrado / Teste ANOVA / Teste de Hipóteses

# Distribuição T de Student
from scipy.stats import t, ttest_1samp
import numpy as np

# função da biblioteca que calcula a probabilidade 'menor que' pela distribuição t de Student
t.cdf(x=1.5, y=8)
# x valor estatística t calculado
# y graus de liberdade (n-1)

# Função que calculo a probabilidade 'maior que'
t.sf(x=1.5, y=8)

# Função que calcula o valor da estatística t automaticamente
salarios = [8000, 8200, 7500, 7700, 7200, 7400, 7900, 8100, 7800, 7600]
t_stat, p_valor = ttest_1samp(salarios, popmean=7500)
# amostra são os dados coletados
# popmean é a média populacional

# calculo manual da estatística t
mp = 7500 # média populacional
x = 8000 # valor alvo
s = 1000 # desvio padrão da amostra
n = 10 # tamanho da amostra
gl = n-1 # graus de liberdade

t_score = (x - mp) / (s / np.sqrt(n))

# -----------------------------------------------------------------

# Distribuição Poisson
from scipy.stats import poisson

poisson.pmf(k=3, mu=2)
# k é o número de eventos
# mu é a média de eventos

# para calcular a probabilidade acumulada (menor ou igual a k)
poisson.cdf(k=3, mu=2)

poisson.sf(k=3, mu=2)
# para calcular a probabilidade maior que k

# -------------------------------------------------------------------

# Distribuição Binomial
from scipy.stats import binom

binom.pmf(k=3, n=10, p=0.5)
# k é o número de sucessos esperados
# n é o número de tentativas (eventos fixos)
# p é a probabilidade de sucesso em cada tentativa (percentual)

# ------------------------------------------------------------------

# Qui-quadrado
from scipy.stats import chi2_contingency
import numpy as np

tabela = np.array([[19, 6], [43, 32]])
teste = chi2_contingency(tabela)
# retorna a estatística qui-quadrado, pvalue, graus de liberdade e valores esperados
# tabela é a tabela de contingência (observados)
# a hipótese nula é que as variáveis são independentes
# a hipótese alternativa é que as variáveis são dependentes
# se o pvalue for menor que 0.05, rejeita-se a hipótese nula
# se o pvalue for maior que 0.05, não rejeita-se a hipótese nula

# ------------------------------------------------------------------

# ANOVA
from scipy.stats import f_oneway
import numpy as np
grupo1 = [23, 21, 18, 25, 27, 30, 22]
grupo2 = [30, 32, 29, 31, 28, 35, 27]
grupo3 = [25, 27, 30, 22, 24, 26, 28]
anova = f_oneway(grupo1, grupo2, grupo3)
# retorna a estatística F e o p-valor




