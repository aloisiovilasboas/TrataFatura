from dash import Dash, html, dash_table
from dash.dash_table import FormatTemplate
import pandas as pd

import plotly.express as px


import config 
from utils import converterPastaOFXemXML, lerTodosXMLemPasta   

arquivos = converterPastaOFXemXML(config.stringFolder)
todasAsTransacoes = lerTodosXMLemPasta(config.stringFolder)

df = pd.DataFrame(todasAsTransacoes)






# Initialize the app
app = Dash(__name__)

money = FormatTemplate.money(2)
FormatTemplate.Scheme

# App layout
app.layout = html.Div([
    html.Div(children='Conta Corrente:'),
    dash_table.DataTable(
        columns=[
        dict(id='TRNTYPE', name='TRNTYPE'),
        dict(id='DTPOSTED', name='DTPOSTED'),
        dict(id='DataConvertida', name='Data'),
        dict(id='ValorConvertido', name='Valor', type='numeric', format=money),
        dict(id='TRNAMT', name='TRNAMT'),
        dict(id='FITID', name='FITID'),
        dict(id='CHECKNUM', name='CHECKNUM'),
        dict(id='REFNUM', name='REFNUM'),
        dict(id='MEMO', name='MEMO'),
    ], style_cell={'textAlign': 'left'},
        data=df.to_dict('records')
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

