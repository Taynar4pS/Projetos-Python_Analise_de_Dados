#Importação do pandas
import pandas as pd
#Importação do Numby
import numpy as np

#Organização da tabela
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
#Arquivo
df = pd.read_csv('clientes_remove_outliers.csv')
print(df.head())

#Mascarar dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')
print('cpf_mascara', df)
#Corrigir datas:
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1990-01-01'))

print('data_atualizada', df['data_atualizada'])

#ajustar a idade com base na data atual
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
df['idade_ajustada'] -= ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] < 100, 'idade_ajustada'] = np.nan

print('idade_ajustada', df['idade_ajustada'])

#Corrigir campos com muitas informações:
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip())
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n'))>  1 else 'Desconhecido')
df['estado_sigla'] = df['endereco'].apply(lambda x: x.split(' / ')[1].strip() if len(x.split('\n'))>  1 else 'Desconhecido')

#verificação da formatação do endereço:
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'Endereço inválido' if len(x) >  50 else x)
print('endereco_curto', df['endereco_curto'])

print('Dados tratados: \n', df.head())
#Renomeando as colunas:
df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco_curto']
df['estado'] = df['estado_sigla']
#Salvando o tratamento
df_salvar = df[['nome','cpf','idade','endereco','estado']]
df_salvar.to_csv('clientes_tratados.csv', index=False)

print('Novo DataFrame: \n', pd.read_csv('clientes_tratados.csv'))