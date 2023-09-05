from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graphy_objects as go 
import pandas as pd 

from app import *
from dash_bootstrap_templates import ThemeSwitchAIO

url_theme1 = dbc.themes.VAPOR
url_theme2 = dbc.themes.FLATLY
template_theme1 = 'vapor'
template_theme2 = 'flatly'

df = pd.read_csv("assets/final_data.csv")
state_options = [{'label': x, 'value': x} for x in df['ESTADO'].unique()]

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Linkedin: Vagas em TI")
            ThemeSwitchAIO(aio_id = 'theme', themes = [url_theme1, url_theme2])
        ]),
        dbc.Col([
            html.H3("Titulo")
        ])
    ])
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id = 'empresa',
                value = [state['label'] for state in state_options[:3]],
                multi = True,
                options = state_options
            )
        ])
    ])
    dbc.Row([
        dbc.Col([
            dcc.Graph(id ='line_graph')
        ]),
    ]),

 #    dbc.Row([
 #        dbc.Col
 #    ])

    dbc.Row([
        dbc.Col([
            html.H3('Gráfico1'),
            html.H3('Input1'),
            dcc.Dropdown(
                id = 'empresa1',
                value = state_options[0]['label'],
                options = state_options
            ),
            dcc.Graph(id = 'box1')
        ]),
        dbc.Col([
            html.H3('Gráfico2'),
            html.H3('Input2'),
            dcc.Dropdown(
                id = 'empresa2',
                value = state_options[0]['label'],
                options = state_options
            ),
            dcc.Graph(id = 'box2')
        ])
    ])
])

@app.callback(
        Output('line_graph', 'figure'),
        Input('empresas', 'value'), 
        Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def line(empresas, toggle):
    templates = template_theme1 if toggle else template_theme2

    df_data = df.copy(deep=True)
    mask = df_data['EMPRESA'].isin(estados)

    fig = px.line(df_data[mask], x = 'DATA', y = 'MÉDIA_APLICAÇÕES', color = 'EMPRESA', template = templates)

    return fig

@app.callback(
    Output('box1', 'figure'),
    Input('empresa1', 'value'), 
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def box1(empresas, toggle):
    templates = template_theme1 if toggle else template_theme2

    df_data = df.copy(deep=True)
    data = df_data[df_data['EMPRESA'].isin([estado])]

    fig = px.box(data[mask], x = 'MÉDIA_APLICAÇÕES', template = templates, title = empresa)

    return fig

if __name__ == '__main__':
    app.run_server(debug = True, port = '8051')