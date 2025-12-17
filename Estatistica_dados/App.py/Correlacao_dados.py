import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('../estatistica_dados/clientes-v3-preparado(2).csv')
print(df)

#Usando o Pandas
print('Estatística do dataframe: \n', df.describe())

print('Estatística de um campo: \n', df[['salario', 'anos_experiencia']].describe())

print('Correlação:\n', df[['salario', 'idade']].corr())

print('Correlação com Normalização:\n', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())
print('Correlação com Padronização:\n', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())
print('Correlação com Padronização:\n', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())

print('Correlação:\n', df[['salario','idade', 'idadeMinMaxScaler','idadeStandardScaler','idadeStandardScaler']].corr())

#regra de negócios: Idade de aposentadoria (altera a correlação)
df_filtro_idade = df[df['idade'] <65]
print('Correlação de clientes menores de 65 anos:\n', df_filtro_idade[['salario', 'idade']].corr())

#Correlação espúria - aumenta com o tempo
df['variavel_espuria'] = np.arange(len(df))
print('Variavel_espuria', df['variavel_espuria'].values)

pearson_corr = df[['salario','idade', 'anos_experiencia','numero_filhos']].corr()
spearman_corr = df[['salario','idade', 'anos_experiencia','numero_filhos']].corr(method='spearman')

print('\nCorrelação de Pearson: \n', pearson_corr)
print('\nCorrelação de Spearman: \n', spearman_corr)