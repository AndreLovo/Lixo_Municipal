#Importando as bibliotecas:

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash_html_components.Div import Div

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import plotly.express as px
pd.options.plotting.backend = "plotly"

from matplotlib.ticker import FuncFormatter
#DataFrame Geral
df = pd.read_excel('C:/Users/André Lovo/OneDrive/Área de Trabalho/Dash_Plotly/df_tabela1.xlsx')

#DataFrame Sao Paulo licença ambiental
lasp=pd.read_excel('C:/Users/André Lovo/OneDrive/Área de Trabalho/Dash_Plotly/df_licenca_sp.xlsx')

#DataFrame tabela licença São Paulo - Mapa
mapa1=pd.read_excel(r'C:/Users/André Lovo/OneDrive/Área de Trabalho/Dash_Plotly/df_tabela21.xlsx', usecols=[2,3,4,5])
mapa1_SP=mapa1[mapa1['estado'] == 'SP']

fig1 = df.plot(
 kind='hist', 
 x='tipo', 
 color='estado')

fig2 = df.plot(
 kind='hist', 
 x='licença ambiental', 
 color='estado')

fig3 = df.plot(
 kind='hist',
 x='impermeabilizacao', 
 color='estado')

fig4 = df.plot(
 kind='hist', 
 x='cobertura', 
 color='estado')

fig5 = df.plot(
 kind='hist', 
 x='drenagem_gas', 
 color='estado') 

 
fig6= df.plot(
 kind='hist', 
 x='uso_gas', 
 color='estado')

fig7 = df.plot(
 kind='hist', 
 x='drenagem_aguas_pluviais',
 color='estado')

fig8 = df.plot(
kind='hist', 
x='recirculacao_chorume',
color='estado')

fig9 = df.plot(
 kind='hist', 
 x='drenagem_chorume',
 color='estado')

fig10 = df.plot(
 kind='hist', 
 x='monitoramento_ambiental',
 color='estado')

fig11 = df.plot(
 kind='hist', 
 x='estado',
 y='Equipamentos públicos usados - Trator de esteiras')

fig12 = df.plot(
 kind='hist', 
 x='estado',
 y='Equipamentos privados - Trator de esteiras')

fig13 = lasp.plot(
 kind='hist',
 x='licença ambiental',
 color='municipio')

fig14 =  df.plot(
 kind='bar', 
 x='estado', 
 y='Equipamentos privados - Trator de esteiras', 
 color='municipio')


fig_mapa1_SP = px.scatter_mapbox(mapa1_SP, lat="latitude", lon="longitude", hover_name="municipio",
                              color_discrete_sequence=["fuchsia"],zoom=3, height=500)
fig_mapa1_SP.update_layout(mapbox_style="open-street-map")




#Criando o Layout HTML dentro do dash HTML

app = dash.Dash(__name__)


app.layout = html.Div(children=[
   html.H1("Dados de Manejo de Resíduos Sólidos Urbanos - 2019"),
   html.Div(children=[
        dcc.Graph(figure=fig1, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig2, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig3, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig4, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig5, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig6, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig7, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig8, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig9, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig10, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig11, style={'display': 'inline-block','width':'50%'}),
        dcc.Graph(figure=fig12, style={'display': 'inline-block','width':'50%'}),
        dcc.Graph(figure=fig13, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig14, style={'display': 'inline-block'}),
        dcc.Graph(figure=fig_mapa1_SP)
   ])
])  


if __name__ == '__main__':
   app.run_server(debug=True)