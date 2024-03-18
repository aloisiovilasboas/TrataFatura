import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import pandas as pd
from streamlit_gsheets import GSheetsConnection


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



def deletouconta():       
        deletados = st.session_state['contasEditor']['deleted_rows']
        print(deletados)
        jaApagados=0
        if deletados:
            for i in deletados:
                st.session_state['contas'].pop(i-jaApagados)
                jaApagados+=1

def deletoucartao():       
        deletados = st.session_state['cartoesEditor']['deleted_rows']
        print(deletados)
        jaApagados=0
        if deletados:
            for i in deletados:
                st.session_state['cartoes'].pop(i-jaApagados)
                jaApagados+=1


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.header("Cartões")
    # Exibe o datastream atualizado
        cartoes = pd.DataFrame(st.session_state['cartoes'], columns=['Nome'])
        st.data_editor(cartoes, width=400, hide_index=True, on_change=deletoucartao, disabled=("Nome", "col2"),  num_rows = 'dynamic',key="cartoesEditor")
    with col2:
        st.header("Contas")
    # Exibe o datastream atualizado
        contas = pd.DataFrame(st.session_state['contas'], columns=['Nome'])
        st.data_editor(contas, width=400, hide_index=True, on_change=deletouconta, disabled=("Nome", "col2"),  num_rows = 'dynamic',key="contasEditor")


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        with st.form("formulariocartoes", clear_on_submit=True):
            novo_cartao = st.text_input('Novo Cartão')
            submitted = st.form_submit_button("Adicionar Cartão")
            if submitted:
                st.session_state['cartoes'].append(novo_cartao)
                st.rerun()
        

    with col2:
        with st.form("formulariocontas", clear_on_submit=True):
         #   st.header("Contas")
            nova_conta = st.text_input('Nova Conta')
            submitted = st.form_submit_button("Adicionar Conta")
            if submitted:
                st.session_state['contas'].append(nova_conta)
                st.rerun()
    
    #st.session_state

with st.container():
    col1, col2, col3 = st.columns(3)
    with col2:
        salvar = st.button("Salvar Alterações", type="primary")        
        if salvar:
            conn.update(data=cartoes, worksheet="cartoes")
            conn.update(data=contas, worksheet="contas")
   
            st.success("Salvo com sucesso!")
            st.cache_data.clear()

    


