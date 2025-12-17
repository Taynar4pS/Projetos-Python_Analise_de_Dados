import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('clientes-v3-preparado (1).csv')
print(df.head(20).to_string())

#Gráfico de barras
plt.figure(figsize=(10,6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='blue') #O.Value_counts é para visualizar apenas os valores e.Plot é para visualização dentro do próprio pandas.
plt.title('Divisão de escolaridade')
plt.xlabel('Nível de educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0) #Rotação do texto do eixo, neste caso seria a rotação da palavra quantidade
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10,6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisão de Escolaridade')
plt.xlabel('Nível de educação')
plt.ylabel('Quantidade')

#Gráfico de pizza
plt.figure(figsize=(10,6))
plt.pie(y, labels=y, autopct='%1.2f%%', startangle=90)
plt.title('Distribuição de nível de educação')
plt.show()

#Gráfico de dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label = 'Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.title('Dispersão de Idade e Salário')
plt.show()

