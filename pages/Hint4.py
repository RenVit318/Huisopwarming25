import streamlit as st

st.title("Hint 4")
answer = st.text_input(label="Antwoord op de puzzel", placeholder='...')
if answer == st.secrets['hint4']:
    st.write("Number 4")
st.image("hints/hint4.jpeg")

