import os
import streamlit as st
import pandas as pd
import re

from utils import lerTodosXMLemPasta, ler_arquivo, apagar_primeiras_linhas, escrever_em_arquivo

# Função para selecionar uma pasta
def select_folder():
    files = st.sidebar.file_uploader("Selecione uma pasta", type=None, accept_multiple_files=True, key=None)
    return files

def converterPastaOFXemXML(caminhoPasta):
    arquivos = [caminhoPasta+'/'+arquivo for arquivo in os.listdir(caminhoPasta) if arquivo.endswith('.ofx') ]
    for arquivo in arquivos:
        conteudo = ler_arquivo(arquivo)
        arquivoxml = re.sub('ofx$', 'xml', arquivo)
        conteudo = apagar_primeiras_linhas(conteudo)
        escrever_em_arquivo(conteudo, arquivoxml)
     

    return arquivos


# Layout do app
st.title('Conta Corrente:')
folder_path = select_folder()

if folder_path:
    arquivos = converterPastaOFXemXML(folder_path)
    todasAsTransacoes = lerTodosXMLemPasta(folder_path)

    df = pd.DataFrame(todasAsTransacoes)

    # Exibir o DataFrame
    st.dataframe(df)
