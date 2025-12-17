#Features são novas variáveis
import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')
print(df.head())

#Transformação logarítmica
df['salario_log'] = np.log(df['salario']) #Lopgpl evita problemas com valores zero

print("\nDataframe após transformar logarítmica para 'salario':\n", df.head())

#Transformação em Box-cox: Tras os dados para normalização, tira os outlines
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1) #+1 faz com que nenhum valor seja negativo.

print("\nDataframe após transformação BoxCox para 'salario':\n", df.head())

#Codificação de Frequência - mistura campos para 'Estado'
estado_freq = df['estado'].value_counts() / len(df) #Value.counts:. Conta quantos itens têm na variável. Len(df):Conta a quantidade de linhas
df['estado_freq'] = df ['estado'].map(estado_freq)

print("\nDataframe após codificação de frequência para 'estado':\n", df.head())

#Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']
print("\nDataframe após codificação de frequência para 'estado':\n", df.head())