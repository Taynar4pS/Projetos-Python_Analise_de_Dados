import pandas as pd

def receber_arquivo(clientes):

#Lê um arquivo CSV do computador e retorna um DataFrame.

    df = pd.read_csv(caminho)   # lê o CSV
    print(df.head().to_string())             # imprime as primeiras linhas
    return df                    # retorna o DataFrame para usar depois

# Chamando a função
caminho = 'C:/Users/User/Downloads/clientes.csv'
df = receber_arquivo(caminho)

#Verifica a quantidade de linhas e colunas:
print('Qtd: ', df.shape)

#Verificar tipos de dados:
print('Tipagem: ', df.dtypes)

#Chegar valores nulos:
print('Valores nulos:\n',df.isnull().sum())

#Organização da tabela
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
