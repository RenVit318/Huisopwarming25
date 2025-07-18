import streamlit as st

st.title("Hint 1")
answer = st.text_input(label="Antwoord op de puzzel", placeholder='...')
if answer == st.secrets['hint1']:
    st.write("Number 1")
st.image("hints/hint1.jpeg")

