import pandas as pd
import numpy as np

pd.set_option('diplay.width', None)
pd.set_option('display.max_coldwidth', None)

df = pd.read_csv('../estatistica_dados/clientes-v3-preparado(2).csv')
print(df)

print('Estatística com Pandas')
print('Média:', df['salario'].mean())
print('Mediana:', df['salario'].median())
print('Variância:', df['salario'].var())
print('Desvio padrão:', df['salario'].std())
print('Moda:', df['salario'].mode())
print('Mínimo:', df['salario'].min())
print('Quartis:', df['salario'].quartile([0.25, 0.5, 0.75]))
print('Máximo:', df['salario'].max())
print('Contagem de não nulos:', df['salario'].value_counts().sum())
print('Soma:', df['salario'].sum())

#Estruturas de dados:
##Array: conjunto de itens de apenas um tipo, fica em linha e não em itens.
print("\nColuna do DataFrame:\n", df['salario'])
print("Array do campo:", df['salario'].values)

print('Estatística com Numpy')
print('Média com coluna:', np.mean(df['salario']))
print('Media com array:', np.median(df['salario'].values))

array_campo = df['salario'].values
print('Mediana:', np.median(array_campo))
print('Variância:', np.var(array_campo))
print('Desvio padrão:', np.std(array_campo))
print('Mínimo:', np.min(array_campo))
print('Quartis:', np.quantile(array_campo, [0.25, 0.5, 0.75]))
print('Porcentagem 25%, 50% e 75%:', np.percentile(array_campo, [25, 50, 75]))
print('Máximo:',  np.max(array_campo))
print('Contagem de não nulos:', np.count_nonzero(array_campo))
print('Soma:',  np.sum(array_campo))
