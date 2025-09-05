# Treinando e testando modelos de regresão linear

# Regressão Linear simples
# Bibliotecas utilizadas
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics as metric
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Base de dados gerada pelo copilot 5000x6
df = pd.read_csv('base_salario.csv')

# Verificando os dados
df.shape()
df.head(10)
df.info()

# Analisando a correlação entre as variáveis e visualizando com um mapa de calor
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt=".2f", cmap="Blues", linewidths=0.5, linecolor='white')
plt.show()
# corr() - Variavel que armazena a correlaçao entre as variáveis numéricas.
# annot=True - Mostra os valores dentro das células do mapa de calor.
# fmt=".2f" - Formata os valores com 2 casas decimais.
# cmap="Blues" - Define a paleta de cores do mapa de calor.
# linewidths=0.5 - Define a largura das linhas que separam as células.

# Dividindo os dados em treino e teste
x = df[['idade']]
y = df[['salario']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify= df.iloc[:,4], random_state=42)
# test_size=0.2 - Define que 20% dos dados serão usados para teste e 80% para treino.
# stratify= df.iloc[:,4] - Estratifica pela variavel indicada.
# random_state=42 - Define uma semente para que a divisão dos dados seja sempre a mesma.

# Criando o modelo de regressão
modelo = LinearRegression()
modelo.fit(x,y)

# Visualizando o modelo pela linha de regressão
plt.scatter(x, y, color='red', label='Idade')
plt.plot(x, modelo.predict(x))

# Testando as previsões
y_pred = modelo.predict(x_test)
modelo.intercept_ + modelo.coef_ * 45

# Avaliando as métricas do modelo
mse = metric.mean_squared_error(y_test, y_pred)
rmse = metric.root_mean_squared_error(y_test, y_pred)
r2 = metric.r2_score(y_test, y_pred)

# -----------------------------------------------------------------
# Regressão Linear Múltipla
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics as metric
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Inserção de mais variáveis no modelo
x2 = df[['idade', 'anos_experiencia', 'nivel_educacional']]
y2 = df[['salario']]

# Dividindo os dados em treino e teste
x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, test_size=0.2, stratify= df.iloc[:,4], random_state=42)

# Criando o modelo de regressão
modelo2 = LinearRegression()
modelo2.fit(x2, y2)

# Testando as previsões
y2_pred = modelo2.predict(x2_test)

# Avaliando as métricas do modelo
mse2 = metric.mean_squared_error(y2_test, y2_pred)
rmse2 = metric.root_mean_squared_error(y2_test, y2_pred)
r2_2 = metric.r2_score(y2_test, y2_pred)

# -----------------------------------------------------------------

