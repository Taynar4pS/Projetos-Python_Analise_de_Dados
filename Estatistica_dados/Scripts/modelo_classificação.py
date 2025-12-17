import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib

df = pd.read_csv('../estatistica_dados/clientes-v3-preparado(2).csv')
print(df)

#Categorizar salário: Acima e abaixo da mediana
df['salario_categoria'] = (df['salario'] > df['salario'].median()).astype(int)

X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']] #Preditor
Y = df['salario_categoria'] #Prever

#Dividir dados: Treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#Criar e treinar o modelo - Regressão logística
modelo_lr = LogisticRegression()
modelo_lr.fit(X_train, y_train)

#Criar e treinar o modelo - Árvore de Decisão
modelo_dt = DecisionTreeClassifier()
modelo_dt.fit(X_train, y_train)

#Prever valores de teste
Y_prev_lr = modelo_lr.predict(X_test)
Y_prev_dt = modelo_dt.predict(X_test)

#Métricas de avaliação - Regressão logística
accuracy_lr = accuracy_score(y_test,Y_prev_lr)
precision_lr = precision_score(y_test,Y_prev_lr)
recall_lr = recall_score(y_test,Y_prev_lr)

print(f"\nAcuracia da Regressão Logística: {accuracy_lr}")
print(f"Precisão da Regressão Logística: {precision_lr}")
print(f"Recall (Sensibilidade) da regressão logística: {recall_lr:.2f}")

#Métricas de avaliação - Regressão logística
accuracy_dt = accuracy_score(y_test,Y_prev_dt)
precision_dt = precision_score(y_test,Y_prev_dt)
recall_dt = recall_score(y_test,Y_prev_dt)

print(f"\nAcuracia da Árvore de Decisão: {accuracy_dt}")
print(f"Precisão da Árvore de Decisão: {precision_dt}")
print(f"Recall (Sensibilidade) da Árvore de Decisão: {recall_dt:.2f}")

joblib.dump(modelo_lr, 'modelo_regressao_logistica.pkl')
joblib.dump(modelo_dt, 'modelo_arvore_de_decisao.pkl')
