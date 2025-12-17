import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler
#Configuração da largura e altura
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')
print(df.head())

df = df.drop(['data','estado','nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis=1)

#Normalização: Muda a escala dos dados - MinMaxScaler.
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

#Para mudar a escala de padrão é só add o feature_range=(novo padrão)
min_max_scaler = MinMaxScaler(feature_range=(-1,1))
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])

#Padronização: Muda o padrão dos dados - StandardScaler: Utiliza a média e o Desvio Padrão
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

#RobustScaler: Utiliza a mediana e o IQR
scaler = RobustScaler()
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])

print(df.head(15))
#std - desvio padrão
print("MinMaxScaler (De 0 a 1):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['idadeMinMaxScaler'].min(),df['idadeMinMaxScaler'].max(),df['idadeMinMaxScaler'].mean(),df['idadeMinMaxScaler'].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(df['salarioMinMaxScaler'].min(),df['salarioMinMaxScaler'].max(),df['salarioMinMaxScaler'].mean(),df['salarioMinMaxScaler'].std()))