import pandas as pd
import numpy as np
from requests import patch
import seaborn as sns
import matplotlib.pyplot as plt

base = pd.read_csv(r'C:\Users\guiac\Downloads\Formação+CD\Formação CD\10.Limpeza e tratamento de Dados - Prática em Python\tempo.csv', sep=';')
df = pd.DataFrame(base)
print(df)

# Substituindo as categorias "verdadeiro" e "falso" da coluna 'Vento' para padronização com a coluna 'Jogar' e substituindo valores faltantes.
df.loc[df['Vento'] == "VERDADEIRO", 'Vento'] = 'sim'
df.loc[df['Vento'] == 'FALSO', 'Vento'] = 'nao'
print(df['Vento'].value_counts())
print(df['Vento'].isna())
df['Vento'].fillna('nao', inplace=True)
print(df)

# Substituindo os outliers da coluna 'Umidade' pela mediana do conjunto.
df.loc[(df['Umidade'] < 0) | (df['Umidade'] > 100), 'Umidade'] = df['Umidade'].median()
mediana = df['Umidade'].median()
df['Umidade'].fillna(mediana, inplace=True)
print(df)

# Substituindo os outliers da coluna 'Temperatura' pela mediana do conjunto.
df['Temperatura'] = df['Temperatura'].astype(float)
df.loc[(df['Temperatura'] < -130) | (df['Temperatura'] > 130), 'Temperatura'] = df['Temperatura'].median()
print(df)

# Substituindo categoria da coluna Aparencia que não pertence ao conjunto.
df.loc[df['Aparencia'] == 'menos', 'Aparencia'] = 'chuva'
print(df['Aparencia'])

print(df)

sns.histplot(df.iloc[:,1], kde=True, bins=4).set(title='Histograma', xlabel='Temperatura', ylabel='Count')
plt.show()

sns.kdeplot(df.iloc[:,1]).set(title='Curva de Densidade')
plt.show()

sns.barplot(df.iloc[:,1], )

barra = sns.barplot(df.iloc[:,1], color='skyblue', edgecolor='black')
barra.set(title="Gráfico de Barra", xlabel='Temperatura', ylabel='Contagem')

for patch in barra.patches:
    altura = patch.get_height() # Calcula a contagem (altura) do rótulo de cada barra e joga na variável.
    barra.text( # Sempre usar o nome da variável com armazena o grafico. 
        # Essa função define o texto com or parâmetros a seguir que devem seguir a ordem:
        patch.get_x() + patch.get_width() / 2, # Captura a lateral esquerda da barra e calcula metade da largura para centralizar o rótulo.
        altura + 0.5, # Determina a altura do rótulo, que no caso é 0.1 acima da altura da barra.
        f'{int(altura)}', # Conteúdo que será exibido no rótulo.
        ha='center', va='bottom', fontsize=10 # Alinhamento e tamanho de fonte.
    )
plt.show()

plt.subplot(2,2,1)
plt.scatter(x=df['Temperatura'], y=df['Umidade'], color='blue', marker='*')
plt.subplot(2,2,2)
plt.scatter(x=df['Temperatura'], y=df['Umidade'], color='blue', marker='*')
plt.subplot(2,2,3)
plt.scatter(x=df['Temperatura'], y=df['Umidade'], color='blue', marker='*')
plt.subplot(2,2,4)
plt.scatter(x=df['Temperatura'], y=df['Umidade'], color='blue', marker='*')
plt.show()

sns.regplot(x=df['Temperatura'], y=df['Umidade'], data=df, color='blue', x_jitter = 0.3, fit_reg=False)
plt.show()

plt.boxplot(df['Temperatura'].dropna().tolist(), vert=False, showfliers=False, notch=True, patch_artist=True)
plt.show()

sns.boxplot(x=df['Temperatura'].dropna(), orient='h', showfliers=False, notch=False)
plt.show()