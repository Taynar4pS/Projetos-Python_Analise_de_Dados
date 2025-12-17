import pandas as pd
import joblib

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../estatistica_dados/clientes-v3-preparado(2).csv')
print(df.isnull().sum().sum())

#Carregar modelo treinado
modelo_regressao_logistica = joblib.load('modelo_regressao_logistica.pkl')
modelo_regressao_linear = joblib.load('modelo_regressao.pkl')
modelo_arvore_decisao = joblib.load('modelo_arvore_de_decisao.pkl')

#Dados dos novos funcionários
dados_novos_funcionarios = pd.DataFrame({
    'idade': [35, 45, 30],
    'anos_experiencia': [6, 12, 5],
    'nivel_educacao_cod': [2, 3, 4],
    'area_atuacao_cod': [1, 4, 3],
})

#Prever o salário com modelo treinado
salario_previsto = modelo_regressao_linear.predict(dados_novos_funcionarios)

for x in range(len(salario_previsto)):
    print(f'Salário Previsto do {x+1}º funcionário: R${salario_previsto[x]:,.2f}')

#Classificar o salário com modelo treinado
categoria_salario = modelo_regressao_logistica.predict(dados_novos_funcionarios)

for x in range(len(salario_previsto)):
    categoria = 'Acima da mediana' if categoria_salario[x] == 1 else 'Abaixo da mediana'
    print(f'Salário Previsto do {x+1}º funcionário: {salario_previsto[x]:,.2f}')