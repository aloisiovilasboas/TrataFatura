import streamlit as st
import numpy as np

import pandas as pd
from io import StringIO
import xml.etree.ElementTree as ET

from utils import limparString, leTransacoes

from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Importar Arquivos", page_icon="📈")


conn = st.connection("gsheets", type=GSheetsConnection)
contasdata = conn.read(worksheet="contas", usecols=[0])
contas =contasdata['Nome'].tolist()
cleanedContas = [x for x in contas if str(x) != 'nan']
if 'contas' not in st.session_state:
    st.session_state['contas'] = cleanedContas

cartoesdata = conn.read(worksheet="cartoes", usecols=[0])
cartoes =cartoesdata['Nome'].tolist()
cleanedCartoes = [x for x in cartoes if str(x) != 'nan']
if 'cartoes' not in st.session_state:
    st.session_state['cartoes'] = cleanedCartoes







st.markdown("# Importar Arquivos")
#st.sidebar.header("Contas")

#contas =['BB', 'CEF', 'NuBank', 'Santander', 'Sicoob', 'Sicredi', 'SulAmérica', 'Unicred', 'XP Investimentos']

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        selecao_contaoucartao = st.selectbox('Importar arquivo de', ["conta corrente", "cartão"])

    with col2:
        if selecao_contaoucartao == "conta corrente":
            conta_selecionada = st.selectbox("Escolha uma conta", cleanedContas)
        else:
            conta_selecionada = st.selectbox("Escolha um cartão", cleanedCartoes)

# Mostrar a conta selecionada
st.write(f"Importar arquivo de {selecao_contaoucartao}: {conta_selecionada}")
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
    st.dataframe(df, column_order=("Data Convertida", "Valor Convertido", "MEMO", "FITID"))

   


st.button("Re-run")