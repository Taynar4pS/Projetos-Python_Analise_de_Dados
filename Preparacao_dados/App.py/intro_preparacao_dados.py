#Inicio de análise exploratória
import pandas as pd

df = pd.read_csv('clientes-v2.csv')
print('cliente_dados-v2.cvs')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors = 'coerce')

print('verificação inicial: ')
#Tras informações das colunas e campos nulos
print(df.info())

print('Analise de dados nulos: \n', df.isnull().sum())
#Para fazer a conta da porcentagem é só colocar o:.mean * 100
print('% de dados nulos:\n', df.isnull().mean() * 100)
#deleta todos os dados nulos
df.dropna(inplace=True)
#Repetir o:.sum() para confirmar se os dados foram realmente removidos
print('Confirmar remoção de dados nulos:\n', df.isnull().sum().sum())

print('Analise de dados duplicados:\n', df.duplicated().sum())

print('Análise de dados únicos:\n', df.nunique())
#Mostra as estatísticas
print('Estatística dos dados:\n', df.describe())

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('clientes-v2-tratados.csv', index=False)