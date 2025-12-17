import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
import joblib

df = pd.read_csv('../estatistica_dados/clientes-v3-preparado(2).csv')
print(df)


X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']] ## Variável que tem no DF, ou seja, o preditor
Y = df['salario'] ##Variavel que vai ser prevista

#Dividir dados: Treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#Criar e treinar modelo - Regressão linear
modelo_lr = LinearRegression()
modelo_lr.fit(X_train, y_train) #Função para treinar a máquina

#Prever valores de teste
Y_prev = modelo_lr.predict(X_test)

#Métricas de avaliação
r2 = r2_score(y_test, Y_prev)
print(f'Coeficiente de Determinação - R²: {r2:.2f}')

rmse = root_mean_squared_error(y_test, Y_prev)
print(f"Raiz do Erro Quadrático Médio - RMSE: {rmse:.2f}")
print(f"Desvio Padrão do campo Salário: {df['salario'].std()}")

#Salvar o modelo
joblib.dump(modelo_lr, 'modelo_regressao.pkl')