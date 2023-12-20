import streamlit as st
import pandas as pd
import config
from utils import converterPastaOFXemXML, lerTodosXMLemPasta

# Função para selecionar uma pasta
def select_folder():
    folder_path = st.sidebar.file_uploader("Selecione uma pasta", type=None, accept_multiple_files=False, key=None)
    return folder_path

# Layout do app
st.title('Conta Corrente:')
folder_path = select_folder()

if folder_path:
    arquivos = converterPastaOFXemXML(folder_path)
    todasAsTransacoes = lerTodosXMLemPasta(folder_path)

    df = pd.DataFrame(todasAsTransacoes)

    # Exibir o DataFrame
    st.dataframe(df)