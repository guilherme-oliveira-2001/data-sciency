# Códigos úteis para análise exploratória dos dados. 

# df.loc[] - Faz uma busca na coluna indicada no parâmetro através de um valor específico.
# df.iloc[] - Semelhante ao .loc, porém o utiliza o índice da linha para buscar na coluna.
# df[].value_counts - Faz a contagem de labels da coluna.
# df.info - Traz informações sobre o tipo de dado de cada coluna e se há valores nulos (NaN).
# df[].isna() - Verifica cada linha da coluna e retorna True ou False se o dado for nulo.
# df[].isna().sum() - Conta quantos valores nulos tem na coluna.
# df[].fillna() - Substitui os valores nulos da coluna.
# df[].fillna().median() - Substitui os valores nulos da coluna pela mediana do conjunto. Com o parâmetro "inplace=True" essa substituição é feita na variável e não apenas na saída.
# df.get_dummies() - Converte colunas categóricas binárias (ex.: sim/não; fem/masc etc) em valor binário.
# df.map({'x': 0, 'y': 1}) - Essa função também converte colunas em valores binários.
# df.rename(columns={'col_antg': 'col_nova'}, inplace=True) - Renomear as colunas.
# df["nova coluna"] = ... - Cria uma nova coluna.
# df.describe() - Retorna uma tabela na saída com vários dados estatísticos da coluna. Ex.: contagem, média, minimo, maximo, mediana, 1º quartil, 3º quartil.
# pandas.crosstab(df['Coluna_x'], df['Coluna_y']) - Faz o cruzamento entre duas colunas para uma análise bidirecional.
# df.corr() - Gera a correlação linear entre as variáveis do dataset, com base na Correlação de Pearson.



