import streamlit as st

st.title("Hint 4")
answer = st.text_input(label="Antwoord op de puzzel", placeholder='...')
if str(answer).lower() == st.secrets['hint4']:
    st.write("The fourth number is ", st.secrets['sol4'])
st.image("hints/hint4.jpeg")

