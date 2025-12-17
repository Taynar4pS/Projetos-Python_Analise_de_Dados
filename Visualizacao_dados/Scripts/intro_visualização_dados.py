import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado (1).csv')
print(df.head().to_string())

#Histograma:
plt.hist(df['salario'])
plt.show() #Para visualizar os dados

#Paramêtros
plt.figure(figsize=(10,6))
#Alpha=Transparência do gráfico
plt.hist(df['salario'],bins=100, color='green', alpha=0.8)
plt.title('Histograma - distribuição de salários')
plt.xlabel('Salário')
plt.xticks(ticks=range(0, int(df['salario'].max()) + 2000,2000))
plt.xlabel('frequência')
plt.grid(True)
plt.show()

#Multiplos gráficos
plt.figure(figsize=(10,6))
plt.subplot(2,2,1) #2 linha, 2 coluna, 1ºGráfico

#Gráfico de dispersão
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão - Salário e Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(1,2,2)
plt.scatter(df['salario'], df['anos_experiencia'], color='red', alpha=0.6, s=30)
plt.title('Dispersão - Idade e Anos de experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de experiência')

#Mapa de Calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2,2,3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Idade')

plt.tight_layout() #Ajusta os espaçamentos
plt.show()