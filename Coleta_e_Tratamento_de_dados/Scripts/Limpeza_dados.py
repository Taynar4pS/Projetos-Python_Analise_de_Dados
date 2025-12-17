import pandas as pd

def receber_arquivo(clientes):

#Lê um arquivo CSV do computador e retorna um DataFrame.

    df = pd.read_csv(caminho)   # lê o CSV
    print(df.head().to_string())             # imprime as primeiras linhas
    return df                    # retorna o DataFrame para usar depois

# Chamando a função
caminho = 'C:/Users/User/Downloads/clientes.csv'
df = receber_arquivo(caminho)

#Organização da tabela
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

#Remoção dos dados, neste caso os dados que não são utilizados no trabalho podem ser removidas da tabela.
df.drop('pais', axis=1, inplace=True)
df.drop(2, axis=0, inplace=True)

#Normalizar os campos: Verificar e definir um padrão para os textos.
df['nome'] = df['nome'].str.title() #Primeira letra Maiúscula e o resto minúsculo
df['endereco'] = df['endereco'].str.lower() #Minuscúlo
df['estado'] = df['estado'].str.upper() #Maiúsculo

#Converter tipo de dados:
df['idade'] = df['idade'].astype(int)

#Verificar tipos de dados:
print('Tipagem: ', df.dtypes)

##Tratar valores nulos (ausentes)
df_fillna = df.fillna(0) #Substituir valores nulos por 0
df_dropna = df.dropna() #Remover registros com valores nulos
df_drona4 = df.dropna(thresh=4) #Mantém valor que tem no mínimo 4 valores não nulos.
df = df.dropna(subset=['cpf']) #Remove registros com qualquer variável nula (neste caso, foi o CPF)

#Campos com valores nulos:
print('Valores nulos:\n',df.isnull().sum())
print('Qtd de registos nulos com fillna:', df.isnull().sum())
print('Qtd de registos nulos com dropna:', df.isnull().sum())
print('Qtd de registos nulos com dropna4:', df.isnull().sum())
print('Qtd de registos nulos com CPF:', df.isnull().sum())

#Substituição quando tem um valor nulo por uma frase:
df['endereco'] = df['endereco'].fillna('Endereço não informado')
#Tratar formado de data:
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce') ##Formato da data

#Tratar valores duplicados:
print('Qtd de registros atual: ', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset = 'cpf', inplace=True)
print('Qtd de registros removendo os dados duplicados: ', len(df))

print('Qts de dados limpos:\n ', df)

#Salvar o dataframe:
df['data'] = df['data_corrigida']
df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo DataFrame: \n', pd.read_csv('clientes_limpeza.csv'))


