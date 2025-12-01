from idlelib.pyshell import usage_msg

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from pandas.io.pytables import Table

df = pd.read_csv('../Python_para_analise_de_dados_atividade_final/ecommerce_estatistica (1).csv')
print(df.columns)

lista_genero = df['Gênero'].unique()
options = [{'label': genero, 'value': genero} for genero in lista_genero]

def cria_graficos(selecao_genero):
    filtro_df = df[df['Gênero'].isin(selecao_genero)]

    fig1 = px.bar(filtro_df, x='Nota', y='Desconto', color='Gênero',color_discrete_sequence=px.colors.qualitative.Vivid, barmode="group")
    fig1.update_layout(
        title='Nota e descontos pela gênero do produto',
        xaxis_title='Nota',
        yaxis_title='Desconto',
        legend_title='Gênero',

    )
    fig2 = px.scatter_3d(filtro_df, x='Qtd_Vendidos', y='Preço', z='Desconto', color='Gênero')
    fig2.update_layout(
            title='Produto vs desconto',
            scene=dict(
                xaxis_title='Qtd_Vendidos',
                yaxis_title='Preço',
                zaxis_title='Desconto',

            ),
        )
    return fig1, fig2

def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Dashboard Interativo",style={'textAlign': 'center', 'color': 'rbda:86, 134, 153'}),
        html.Div('''
        Interatividade entre os dados.
        '''),
        html.Br(),
        html.H2("Gráfico de produto de acordo com o desconto",style={'textAlign': 'center', 'color': 'rbda:86, 134, 153'}),
        dcc.Checklist(
            id='id_selecao_genero',
            options=options,
            value=[lista_genero[0]],
        ),

        dcc.Graph(id='id_grafico_3d'),
        dcc.Graph(id='id_grafico_barra'),

    ])
    return app
#Executa o app
if __name__ == '__main__':
    app = cria_app()

    @app.callback(
       [
            Output('id_grafico_barra', 'figure'),
            Output('id_grafico_3d', 'figure'),
    ],
        [Input('id_selecao_genero', 'value')]
    )
    def atualiza_graficos(selecao_genero):
        fig1, fig2 = cria_graficos(selecao_genero)
        return fig1, fig2
    app.run(debug=True, port=8052)
