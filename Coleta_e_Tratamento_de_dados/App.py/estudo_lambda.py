import pandas as pd
#Expressão Lambda calcula o cubo de um número:
eleva_cubo_lambda = lambda x: x ** 3
print (eleva_cubo_lambda(2))

#Utilizar a função com operações simples:
df = pd.DataFrame({'números': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]})

df['cubo_funcao'] = df['números'].apply(eleva_cubo_lambda)
df['cubo_lambda'] = df['números'].apply(lambda x: x ** 3)
print(df)
#Para operações complexas, utilizar funções.