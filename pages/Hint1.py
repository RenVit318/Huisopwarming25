import streamlit as st

if str(st.session_state.first_pass).lower() != st.secrets['first_pass']:
    st.write('Wat doe je hier?? Ga terug naar de hoofdpagina!!')
    st.stop()
    
st.title("Hint 1")
answer = st.text_input(label="Antwoord op de puzzel", placeholder='...')
if answer == st.secrets['hint1']:
    st.write("The first number is ", st.secrets['sol1'])
st.image("hints/hint1.jpeg")

