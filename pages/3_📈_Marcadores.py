import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar






marcadoresDefault = ['Deso', 'Energisa', 'Two']
 

if 'marcadores' not in st.session_state:
    marcadoresValue = marcadoresDefault
else:
    marcadoresValue = st.session_state.marcadores

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


marcadoresNaTela = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=marcadoresValue,
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags=20,
    key="marcadoresNaTela")

st.session_state.marcadores = marcadoresNaTela


if 'a_counter' not in st.session_state:
    st.session_state.a_counter = 0

st.write("### Counter:")
st.write(st.session_state.a_counter)

button = st.button("Increment Counter")
if button:
    st.session_state.a_counter += 1
    "apertou",st.session_state.a_counter


st.write("### Session State:")
st.write(st.session_state)


maxtags_sidebar = st.sidebar.slider('Number of tags allowed?', 1, 10, 3, key='1')


keyword = st_tags_sidebar(label='# Enter Keywords:',
                          text='Press enter to add more',
                          value=['Zero', 'One', 'Two'],
                          suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
                          maxtags=maxtags_sidebar,
                          key="afrfae")

st.sidebar.write("### Results:")
st.sidebar.write((keyword))

