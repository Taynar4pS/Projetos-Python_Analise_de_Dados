# 📊 Dashboard Interativo com Dash e Plotly

## 📝 Propósito do Projeto
Este projeto tem como objetivo criar um **dashboard interativo** utilizando **Dash**, **Plotly Express** e **Pandas**, permitindo explorar dados de um dataset de e-commerce.  
O dashboard possibilita:

- Filtragem dinâmica de gênero;
- Gráfico de barras comparando Nota x Desconto;
- Gráfico 3D interativo mostrando Preço, Quantidade Vendida e Desconto;
- Tabela dinâmica com filtragem por preço.

O projeto serve como estudo e como base para dashboards profissionais de análise de dados.

---

## 📂 Estrutura do Projeto
```
├── app.py                          # Arquivo principal da aplicação Dash
├── imagens/                        # imagens 
├── DataSet                         # Base de dados utilizada
└── README.md                       # Este arquivo
```
---

## 🧠 Tecnologias Utilizadas

- Python 3.10+
- Dash
- Plotly Express
- Pandas

---

## 📦 Como Reproduzir o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```
### 2️⃣ Crie e ative o ambiente virtual
```bash
pip install -r requirements.txt
```
Windows:
```bash
.venv\Scripts\activate
```
Mac/Linux:
```bash
source .venv/bin/activate
```
### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```
Se você não tiver o requirements.txt, ele deve conter:
```bash
dash
pandas
plotly
```
### 4️⃣ Execute o aplicativo
```bash
python app.py
```
### 5️⃣ Acesse no navegador
```bash
http://127.0.0.1:8052/
```
## 📊 Funcionalidades — Implementação em Código

### ✔️ 1. Filtro de Gênero
Permite selecionar os gêneros disponíveis no dataset.

```python
lista_genero = df['Gênero'].unique()
options = [{'label': genero, 'value': genero} for genero in lista_genero]

dcc.Checklist(
    id='id_selecao_genero',
    options=options,
    value=[lista_genero[0]]
)
```
✔️ 2. Gráfico de Barras — Nota x Desconto

Mostra como os descontos variam de acordo com a nota do produto, separados por gênero.
def cria_graficos(selecao_genero):
    filtro_df = df[df['Gênero'].isin(selecao_genero)]
```
    fig1 = px.bar(
        filtro_df,
        x='Nota',
        y='Desconto',
        color='Gênero',
        barmode='group',
        color_discrete_sequence=px.colors.sequential.Purples
    )
    fig1.update_layout(
        title='Nota e descontos pela gênero do produto',
        xaxis_title='Nota',
        yaxis_title='Desconto',
        legend_title='Gênero'
    )
```
✔️ 3. Gráfico 3D — Quantidade Vendida, Preço e Desconto

Visualiza três variáveis ao mesmo tempo com separação por gênero.
```
fig2 = px.scatter_3d(
    filtro_df,
    x='Qtd_Vendidos',
    y='Preço',
    z='Desconto',
    color='Gênero'
)
fig2.update_layout(
    title='Produto vs desconto',
    scene=dict(
        xaxis_title='Qtd_Vendidos',
        yaxis_title='Preço',
        zaxis_title='Desconto'
    )
)
return fig1, fig2
```
✔️ 4. Tabela Dinâmica — Filtragem por Preço

Gera uma tabela HTML com as linhas filtradas pelo valor selecionado.
```
def tabelas_dash(selecao_preco, max_rows=10):
    filtro_df = df[df['Preço'].isin(selecao_preco)]
    filtro_df = filtro_df.head(max_rows)

    return html.Table([
        html.Thead(html.Tr([html.Th(col) for col in filtro_df.columns])),
        html.Tbody([
            html.Tr([
                html.Td(filtro_df.iloc[i][col]) for col in filtro_df.columns
            ]) for i in range(len(filtro_df))
        ])
    ])
```
✔️ 5. Callback — Atualização Automática dos Gráficos

Conecta o checklist aos gráficos, atualizando tudo em tempo real.
```
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
```
✔️ 6. Estrutura do Layout do App

Define os componentes que aparecem no dashboard.
```
app.layout = html.Div([
    html.H1("Dashboard Interativo"),
    html.H2("Gráfico de produto de acordo com o desconto"),

    dcc.Checklist(
        id='id_selecao_genero',
        options=options,
        value=[lista_genero[0]]
    ),

    dcc.Graph(id='id_grafico_barra'),
    dcc.Graph(id='id_grafico_3d'),
])
```
