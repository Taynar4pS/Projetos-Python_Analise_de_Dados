import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado (1).csv')
print(df.head().to_string())

#Gráfico de dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter')
plt.show()

#Gráfico de densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['salario'], fill=True, color='#863e9c')
plt.title('Densidade de Salários')
plt.xlabel('Salário')
plt.show()

#Gráfico de Pairplot - Dispersão e Histograma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
plt.show()

#Gráfico de regressão
sns.regplot(x='idade', y='salario', data=df, color = '#278f65', scatter_kws={'alpha':0.5, 'color': '#34c289'})
plt.title('Regressão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

#Gráfico countplot com hue=Agrupamento
sns.countplot(x='estado_civil',hue = 'nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado')
plt.ylabel('Quantidade de clientes')
plt.legend(title='Nível de Educação')
plt.show()

