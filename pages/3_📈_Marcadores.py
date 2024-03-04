import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet="marcadores")
st.dataframe(data)


# Inicializa o datastream se ele não existir
if 'nomesfiltros' not in st.session_state:
    st.session_state['nomesfiltros'] = []
if 'termosfiltros' not in st.session_state:
    st.session_state['termosfiltros'] = []
if 'marcadoresFiltros' not in st.session_state:
    st.session_state['marcadoresFiltros'] = []

if 'marcadores' not in st.session_state:
    st.session_state['marcadores'] = []

    

col1, col2 = st.columns(2)

with col1:
    with st.form("my_form", clear_on_submit=True):
        st.header("Filtros")
        # Entrada de texto para adicionar uma nova palavra
        novo_termo = st.text_input('Insira o termo a ser filtrado')
        novo_filtro = st.text_input('Insira o nome do filtro')
        options = st.multiselect(
            'Aplicar marcadores',
            st.session_state['marcadores'],
            [])

            # Botão para adicionar a nova palavra ao datastream
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state['nomesfiltros'].append(novo_filtro)
            st.session_state['termosfiltros'].append(novo_termo)
            st.session_state['marcadoresFiltros'].append(options)
# Exibe o datastream atualizado
    dff = pd.DataFrame({'nomesfiltros':st.session_state['nomesfiltros'], 'termosfiltros':st.session_state['termosfiltros'], 'marcadoresDosFiltros':st.session_state['marcadoresFiltros']})
    st.data_editor(dff, hide_index=True, num_rows = 'dynamic', key="dff")


#CRUD Filtros
   

with col2:
    with st.form("my_formarcadores", clear_on_submit=True):
        st.header("Marcadores")
        # Entrada de texto para adicionar uma nova palavra
        novo_marcador = st.text_input('Insira um novo marcador')

            # Botão para adicionar a nova palavra ao datastream
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state['marcadores'].append(novo_marcador)
            st.rerun()
# Exibe o datastream atualizado
    dfm = pd.DataFrame(st.session_state['marcadores'], columns=['nome'])
    st.write(edited_dfm = st.data_editor(dfm, hide_index=True,key="dfm"))

    st.session_state




