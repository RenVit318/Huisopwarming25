import streamlit as st

st.title("Hint 3")
answer = st.text_input(label="Antwoord op de puzzel", placeholder='...')
if answer == st.secrets['hint3']:
    st.write("Number 3")
st.image("hints/hint3.jpeg")

