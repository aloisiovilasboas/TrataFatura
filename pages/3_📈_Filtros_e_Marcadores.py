import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import pandas as pd
from streamlit_gsheets import GSheetsConnection


conn = st.connection("gsheets", type=GSheetsConnection)


marcadoresdata = conn.read(worksheet="marcadores", usecols=[0])
marcadores =marcadoresdata['Nome'].tolist()
cleanedMarcadores = [x for x in marcadores if str(x) != 'nan']
if 'marcadores' not in st.session_state:
    st.session_state['marcadores'] = cleanedMarcadores



def deletoumarcador():       
        deletados = st.session_state['marcadoresEditor']['deleted_rows']
        print(deletados)
        jaApagados=0
        if deletados:
            for i in deletados:
                st.session_state['marcadores'].pop(i-jaApagados)
                jaApagados+=1

def deletoufiltro():       
        deletados = st.session_state['filtrosEditor']['deleted_rows']
        print(deletados)
        jaApagados=0
        if deletados:
            for i in deletados:
                st.session_state['nomesFiltros'].pop(i-jaApagados)
                st.session_state['termosFiltros'].pop(i-jaApagados)
                st.session_state['marcadoresFiltros'].pop(i-jaApagados)
                jaApagados+=1            



filtrosdata = conn.read(worksheet="filtros", usecols=[0,1,2])
nomesFiltros =filtrosdata['Nome'].tolist()
cleanednomesFiltros = [x for x in nomesFiltros if str(x) != 'nan']
if 'nomesFiltros' not in st.session_state:
    st.session_state['nomesFiltros'] = cleanednomesFiltros
termosFiltros =filtrosdata['Termo'].tolist()
cleanedtermosFiltros = [x for x in termosFiltros if str(x) != 'nan']
if 'termosFiltros' not in st.session_state:
    st.session_state['termosFiltros'] = cleanedtermosFiltros
marcadoresFiltros =filtrosdata['Marcadores'].tolist()
cleanedmarcadoresFiltros = [x[2:-2].split("', '") for x in marcadoresFiltros if str(x) != 'nan']
if 'marcadoresFiltros' not in st.session_state:
    st.session_state['marcadoresFiltros'] = cleanedmarcadoresFiltros



    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.header("Filtros")
        filtros = pd.DataFrame({'Nome':st.session_state['nomesFiltros'], 'Termo':st.session_state['termosFiltros'], 'Marcadores':st.session_state['marcadoresFiltros']})
        st.data_editor(filtros, width=400, hide_index=True , on_change=deletoufiltro,  disabled=('Nome','Termo','Marcadores'), num_rows = 'dynamic', key="filtrosEditor")
    with col2:
        st.header("Marcadores")
    # Exibe o datastream atualizado
        marcadores = pd.DataFrame(st.session_state['marcadores'], columns=['Nome'])
        st.data_editor(marcadores, width=400, hide_index=True, on_change=deletoumarcador, disabled=("Nome", "col2"),  num_rows = 'dynamic',key="marcadoresEditor")


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        with st.form("my_form", clear_on_submit=True):
          #  st.header("Filtros")
            # Entrada de texto para adicionar uma nova palavra
            novo_termo = st.text_input('Insira o termo a ser filtrado')
            novo_filtro = st.text_input('Insira o nome do filtro')
            options = st.multiselect(
                'Aplicar marcadores',
                st.session_state['marcadores'],
                [])            
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.session_state['nomesFiltros'].append(novo_filtro)
                st.session_state['termosFiltros'].append(novo_termo)
                st.session_state['marcadoresFiltros'].append(options)       
                st.rerun()
    with col2:
        with st.form("my_formarcadores", clear_on_submit=True):
          #  st.header("Marcadores")
            novo_marcador = st.text_input('Insira um novo marcador')
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.session_state['marcadores'].append(novo_marcador)
                st.rerun()

with st.container():
    col1, col2, col3 = st.columns(3)
    with col2:
        salvar = st.button("Salvar Alterações", type="primary")        
        if salvar:
            conn.update(data=marcadores, worksheet="marcadores")
            conn.update(data=filtros, worksheet="filtros")
            st.success("Salvo com sucesso!")
            st.cache_data.clear()

        

    #st.session_state



    


