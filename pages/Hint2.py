import streamlit as st

st.title("Hint 2")
answer = st.text_input(label="Antwoord op de puzzel", placeholder='...')
if answer == st.secrets['hint2']:
    st.write("Number 2")
st.image("hints/hint2.jpeg")

