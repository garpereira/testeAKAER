#necessario ter instalado pandas, dash, plotly
#pip install pandas
#pip install dash
#pip install plotly

from datetime import date, datetime
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


# path_file1 = ".\\HIST_PAINEL_COVIDBR_2022_Parte2_05out2022.csv"
# path_file2 = ".\\HIST_PAINEL_COVIDBR_01dez2020.csv"
path_file3 = '.\\HIST_PAINEL_COVIDBR_DATASET.csv'

#base de dados carregada
df = pd.read_csv(path_file3, on_bad_lines='skip', delimiter=';')
df = pd.DataFrame(df)

#construindo o grafico
fig = px.line(df , x='data', y='obitosNovos', color='estado')

#definindo os dropdown de estado e municipios
opcoes_estadoDropdown = list(df['estado'].unique())
opcoes_yaxisDropdown = ['obitosNovos', 'casosNovos', 'Recuperadosnovos', 'emAcompanhamentoNovos']
#adicionando a opção para listar todos
opcoes_estadoDropdown.append('Todos os Estados')

#retirando valores vazios das listas
opcoes_estadoDropdown = [i for i in opcoes_estadoDropdown if str(i) != 'nan']

#caixa de layout
app.layout = html.Div(children=[
    
    html.H1(children='Painel Covid19'),
    html.H2(children='Gráfico com dados oficiais retirados do DataSuS'),

    html.Div(children='''
        Aplicação criada com Dash para a candidatura de estágio
    '''),

    dcc.Graph(
        id='grafico_dashboard',
        figure=fig
    ),

    html.H3(children='Estado'),
    html.Div(
        
        dcc.Dropdown(
            opcoes_estadoDropdown, value='Todos os Estados', id='estado-dropdown'
        )
    ),

    html.Br(),


    html.H3(children='Valor mostrado no eixo Y'),
    html.Div(
        
        dcc.Dropdown(
            opcoes_yaxisDropdown, value='obitosNovos', id='yaxis-dropdown'
        )
    ),

    html.Br(),

    html.H3(children='Range de data'),
    html.Div(
        dcc.DatePickerRange(
            id='date-range',
            minimum_nights=5,
            clearable=True,
            with_portal=True,
            #no dashboard as datas estao no formato MM/DD/YYYY
            display_format = 'DD/MM/YYYY',

            min_date_allowed= date(2020, 1, 12),
            max_date_allowed = date(2020, 12, 1),
            start_date = date(2020, 1, 12),
            end_date = date(2020, 12, 1)
        )
    )
])

#callbacks functions
@app.callback(
    Output('grafico_dashboard', 'figure'),
    Input('estado-dropdown', 'value'),
    Input('yaxis-dropdown', 'value'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date'),
)

def estados_update(estadoValue, yaxisValue, start_date, end_date):
    # print(f'start -> {start_date}')
    # print(f'end -> {end_date}')
    # print(f"df -> {df['data'][1]}\n")

    df_auxiliar = df.copy()

    start_date_object = date.fromisoformat(start_date)
    end_date_object = date.fromisoformat(end_date)
    start_date_string = start_date_object.strftime('%m/%d/%Y')
    end_date_string = end_date_object.strftime('%m/%d/%Y')

    condicao = (df_auxiliar['data'] >= start_date_string) & (df_auxiliar['data'] <= end_date_string)
    df_auxiliar = df_auxiliar.loc[condicao, :]
 
    if estadoValue == 'Todos os Estados':
        fig = px.line(df_auxiliar, x='data', y=str(yaxisValue), color='estado')

    else:
        tabela_filtrada = df_auxiliar.loc[df_auxiliar['estado'] == estadoValue, :]
        fig = px.line(tabela_filtrada , x='data', y=str(yaxisValue), color='estado')

    return fig

if __name__ == '__main__':
    # app.run_server(dev_tools_hot_reload=False)
    app.run_server(debug=True)
