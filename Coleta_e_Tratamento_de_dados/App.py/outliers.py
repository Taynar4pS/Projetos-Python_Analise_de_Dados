#importação do pandas
import pandas as pd
#importação do pacote da scipy:
from scipy import stats
#Organização das colunas
pd.set_option('display.max_columns', None)
#DataFrame limpo:
df = pd.read_csv('clientes_limpeza.csv')

#Primeiro Filtro
df_filtro_basico = df[df['idade'] > 100]
print(df_filtro_basico)

##Identificar outliers com o Z-score
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]
print("Outliers pelo Z-score:\n", outliers_z)

##Filtrar com outliers com Z-score - Utilizando o desvio padrão
df_zscore = df[(stats.zscore(df['idade']) <3)]
##Identificar o outliers com IQL - Divisão em quadrantes
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print("Limites IQR: ", limite_alto, limite_baixo)

#Filtrar outliers com IQR
limite_baixo = 1
limite_alto = 100
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

#Filtrar endereço inválido
df['endereco'] = df['endereco'].apply(lambda x:'Endereço inválido' if len(x.split('\n')) < 3 else x)
print('Qtd de endereços inválidos: ', (df['endereco'] == 'Endereço inválido').sum())
print('Dados tratados com outliers:\n', df)

#Salvar DataFrame
df.to_csv('clientes_remove_outliers.csv', index=False)
print('Novo DataFrame: \n', pd.read_csv('clientes_remove_outliers.csv'))