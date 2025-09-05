# Gráficos úteis para análise de dados Seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = ['exemplo']
# Histograma
sns.histplot(df.iloc[:,1], kde=True, bins=4).set(title='Histograma', xlabel='Coluna_x', ylabel='Coluna_y')
plt.show()
# :,1 - Primeiro valor antes da virgula são as linhas, no caso, todas (:), e o número 1 é a 1ª coluna do data set.
# kde=True - Plota uma linha de suavização para demonstrar a distribuição. Mais clean de visualizar do que a diferença entre as barras.
# bins=4 - Bins são as barras. No caso sendo 4, o histograma estratifica os valores da coluna do eixo x para 4 labels apenas.
# Title - Título.
# xlabel - Título do eixo x.
# ylabel - Título do eixo y.
# xlim(min, max) - Valores da escala (eixo x).
# ylim(min, max) - Valores da escala (eixo y).

# -------------------------------------------------------------------------------------------------------------------------------

# KDE - Curva de Densidade
sns.kdeplot(df.iloc[:,1]).set(title='Curva de Densidade')
plt.show()
# É possível plotar somente o kde sem estar no histograma, pois é mais suave visualmente.

# -------------------------------------------------------------------------------------------------------------------------------

# Boxplot
plt.boxplot(df['Coluna_x'].dropna().tolist(), vert=False, showfliers=True, notch=True, patch_artist=True)
plt.show()
# dropna().tolist() - Remove os valores nulos e converte a coluna do dataframe para uma lista, assim reorganizando os índices.
# vert=False - Indica se o gráfico será plotado verticalmente (True) ou horizontalmente (False).
# showfliers=True - Mostra os outliers no gráfico como bolinhas antes do mínimo e/ou depois do máximo. 
# notch=True - Faz um corte ao centro do gráfico, na mediana, para facilitar a visualização.
# patch_artist=True - Parâmetro que permite estilizar o interior da caixa.
# xlim(min, max) - Valores da escala (eixo x).

# -------------------------------------------------------------------------------------------------------------------------------

# Gráfico de Dispersão
sns.regplot(x=df['coluna_x'], y=df['coluna_y'], data=df, color='blue', x_jitter = 0.3, fit_reg=False)
plt.show()
# data=df - Dados a serem plotados.
# color=blue = Cor dos pontos dispersos.
# x_jitter = 0.3 - Alguns pontos podem ficar sobrepostos, então este parâmetro faz um afastamento suave para que seja possível enxergar os pontos próximos.
# fit_reg=False - Plota a linha de tendência da regressão. O próprio seaborn calcula a melhor reta de aproximação.
# xlim(min, max) - Valores da escala (eixo x).
# ylim(min, max) - Valores da escala (eixo y).

# -------------------------------------------------------------------------------------------------------------------------------

# Gráfico de barras
sns.barplot(df.iloc[:,1], color='skyblue', edgecolor='black').set(title="Gráfico de Barra", xlabel='Coluna_x', ylabel='Coluna_y')
plt.show()
# :,1 - Primeiro valor antes da virgula são as linhas, no caso, todas (:), e o número 1 é a 1ª coluna do data set.
# color='blue' - Cor das barras.
# edgecolor='black' - Cor da borda das barras.
# title - Título do gráfico.
# xlabel - Título do eixo x.
# ylabel - Título do eixo y.
# xlim(min, max) - Valores da escala (eixo x).
# ylim(min, max) - Valores da escala (eixo y).

# -------------------------------------------------------------------------------------------------------------------------------

# Inserir rótulos de dados
barra = sns.barplot(df.iloc[:,1], color='skyblue', edgecolor='black')
barra.set(title="Gráfico de Barra", xlabel='Coluna_x', ylabel='Coluna_y')

for patch in barra.patches:
    altura = patch.get_height()
    barra.text(
        patch.get_x() + patch.get_width() / 2,
        altura + 0.5,
        f'{int(altura)}',
        ha='center', va='bottom', fontsize=10
    )
plt.show()

# for patch in barra.patches: - O "for" é para percorrer cada barra (bin) do gráfico. 
# altura = patch.get_height() - Conta o valor de cada barra (altura) para inserir como rótulo.
# barra.text() - Usar sempre o nome da variável que armazena o gráfico. Essa função .text define o texto com os parâmetros a seguir que devem seguir a ordem:
# patch.get_x() + patch.get_width() / 2, # Captura a lateral esquerda da barra e calcula metade da largura para centralizar o rótulo.
# altura + 0.5, # Determina a altura em que o rótulo ficará posicionado, que no caso é 0.1 acima da altura da barra.
# f'{int(altura)}' - Conteúdo que será exibido no rótulo. É necessária essa conversão para int, pois como é o produto de uma divisão, ele vem como float.
# ha='center', va='bottom', fontsize=10  - ha alinhamento horizontal, va alinhamento vertical e fontsize tamanho da fonte.

# ------------------------------------------------------------------------------------------------------------------------------

# Plotagem de vários gráficos na mesma figura
plt.subplot(2,2,1)
plt.scatter(x=df[''], y=df['Umidade'], color='blue', marker='*')
plt.subplot(2,2,2)
plt.scatter(x=df['Temperatura'], y=df['Umidade'], color='blue', marker='*')
plt.subplot(2,2,3)
plt.scatter(x=df['Temperatura'], y=df['Umidade'], color='blue', marker='*')
plt.subplot(2,2,4)
plt.scatter(x=df['Temperatura'], y=df['Umidade'], color='blue', marker='*')
plt.show()

# ('2',2,1) - o primeiro número "2" indica a quantidade de gráficos por linha.
# (2,'2',1) - o segundo número "2" indica a quantidade de gráficos por coluna.
# (2,2,'1') - o número "1" indica a posição do 1º gráfico, da esquerda para a direita.
# Logo, nesse parâmetro de exemplos, seria uma matriz 2x2, ou seja, 4 gráficos, com o último número do parâmetro indicando a posição do 1º gráfico.

# -----------------------------------------------------------------------------------------------------------------------------

