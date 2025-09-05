import pandas as pd
import numpy as np

base = pd.read_csv("tempo.csv", sep=';')
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
