from dash import Dash, html, dash_table, dcc
from dash.dash_table import FormatTemplate
import pandas as pd
import xml.etree.ElementTree as et 
import plotly.express as px
import os
import re

def converterPastaOFXemXML(caminhoPasta):
    arquivos = [caminhoPasta+'/'+arquivo for arquivo in os.listdir(caminhoPasta) if arquivo.endswith('.ofx') ]
    for arquivo in arquivos:
        conteudo = ler_arquivo(arquivo)
        arquivoxml = re.sub('ofx$', 'xml', arquivo)
        conteudo = apagar_primeiras_linhas(conteudo)
        escrever_em_arquivo(conteudo, arquivoxml)
     
        


    return arquivos

def apagar_primeiras_linhas(texto, num_linhas=10):
    linhas = texto.split('\n')
    novo_texto = '\n'.join(linhas[num_linhas:])
    return novo_texto

def ler_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='ISO-8859-14') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo '{caminho_arquivo}': {e}")
        return None


def escrever_em_arquivo(texto, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)











def transform_xml(xmlroot):
    transacoes = []
    for child in xmlroot:
        if child.tag == "STMTTRN":
            transacao={}
            for tagtransacao in child:
                if tagtransacao.tag=="DTPOSTED":
                    data_string = tagtransacao.text[:-14]
                    date = pd.to_datetime(data_string, format='%Y%m%d')
                    transacao.update({'DataConvertidadt': date}) 
                    transacao.update({'DataConvertida': date.strftime('%d/%m/%Y')}) 
                else:
                    if tagtransacao.tag=="TRNAMT":
                        transacao.update({'ValorConvertido': pd.to_numeric(tagtransacao.text)})
                transacao.update({tagtransacao.tag: tagtransacao.text})
            transacoes.append(transacao)
    
    return transacoes

def lerTodosXMLemPasta(caminhoPasta):
    arquivos = [caminhoPasta+'/'+arquivo for arquivo in os.listdir(caminhoPasta) if arquivo.endswith('.xml') ]
    todasAstransacoes =[]
    for arquivo in arquivos:
        etree = et.parse(arquivo)
        eroot = etree.getroot()
        transactions = eroot[1][0][2][2]
        transacoes = transform_xml(transactions)
        todasAstransacoes = todasAstransacoes+transacoes
    return todasAstransacoes

files = converterPastaOFXemXML('comprovantes2023/bb/2023')
todasAsTransacoes = lerTodosXMLemPasta('comprovantes2023/bb/2023')
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

