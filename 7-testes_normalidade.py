# Teste de Normalidade Teste de Hipótese
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm, skewnorm

dados= list(set(list(range(150))))

# Histograma
sns.histplot(dados, bins=6)
plt.show()

# -------------------------------------------------------------------------------------------------------------------------------------------------

# QQ Plot
fig, ax = plt.subplots()
stats.probplot(dados, fit=True, plot=ax)
plt.title('Dados')
# Esse gráfico compara os dados de uma amostra com os dados de uma distribuição teórica, que pode ser a normal. O gráfico plota uma linha reta para comparar se os dados da amostra de aproxima da distribuição em questão (normal). Se os dados formam uma linha reta, alinhada a linha plitada pelo gráfico, os dados estão normalmente distribuídos. Caso a distribuição tenha um afastamento nas bordas, é provável que os dados não sejam normalmente distribuídos.

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Teste de Hipótese - Shapiro-Wilk
x = stats.shapiro(dados)
print(x)
# Essa função retorna dois valore, que são: statistics - que analisa o quão diferentes os dados são em comparação com uma distribuição normal e p_value - probabilidade de os dados serem normais. Caso p_value seja maior 0.05, não rejeitamos a hipótese de normalidade, caso menor, rejeita-se a hipótese, logo, os dados não são normais.