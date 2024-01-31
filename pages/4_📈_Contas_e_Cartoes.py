import streamlit as st
import numpy as np


import pandas as pd
from io import StringIO


import xml.etree.ElementTree as ET

from utils import limparString, leTransacoes



st.set_page_config(page_title="Contas e Cartões", page_icon="📈")

st.markdown("# Contas")
st.sidebar.header("Contas")

contas =['BB', 'CEF', 'NuBank', 'Santander', 'Sicoob', 'Sicredi', 'SulAmérica', 'Unicred', 'XP Investimentos']

# Widget para selecionar a conta
conta_selecionada = st.sidebar.selectbox("Escolha uma conta", contas)

# Mostrar a conta selecionada
st.header(f"Esta é a conta {conta_selecionada}")
# coloque o código para mostrar as informações da conta aqui






uploaded_file = st.file_uploader("Selecione um arquivo")
if uploaded_file is not None:
        # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode('ISO-8859-14'))
    string_data = stringio.read()
    string_data2 = limparString(string_data)
    # st.write(string_data2)

    todasAstransacoes =[]
    
    etree = ET.fromstring(string_data2)
    eroot = etree #.getroot()
    transactions = eroot[1][0][2][2]
    transacoes = leTransacoes(transactions)
    todasAstransacoes = todasAstransacoes+transacoes
    df = pd.DataFrame(todasAstransacoes)
    st.dataframe(df)

   


st.button("Re-run")