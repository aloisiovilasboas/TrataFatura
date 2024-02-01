import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import pandas as pd


# Inicializa o datastream se ele não existir
if 'filtros' not in st.session_state:
    st.session_state['filtros'] = []
if 'marcadoresDosFiltros' not in st.session_state:
    st.session_state['marcadoresDosFiltros'] = []

if 'marcadores' not in st.session_state:
    st.session_state['marcadores'] = []

    

col1, col2 = st.columns(2)

with col1:
    with st.form("my_form", clear_on_submit=True):
        st.header("Filtros")
        # Entrada de texto para adicionar uma nova palavra
        novo_filtro = st.text_input('Insira um novo filtro')
        options = st.multiselect(
            'Aplicar marcadores',
            st.session_state['marcadores'],
            [])

            # Botão para adicionar a nova palavra ao datastream
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state['filtros'].append(novo_filtro)
            st.session_state['marcadoresDosFiltros'].append(options)
# Exibe o datastream atualizado
    dff = pd.DataFrame({'filtros':st.session_state['filtros'], 'marcadoresDosFiltros':st.session_state['marcadoresDosFiltros']})
    st.data_editor(dff, hide_index=True, num_rows = 'dynamic', disabled=['filtros', 'marcadoresDosFiltros'])


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




