import streamlit as st

if str(st.session_state.first_pass).lower() != st.secrets['first_pass']:
    st.write('Wat doe je hier?? Ga terug naar de hoofdpagina!!')
    st.stop()
    
st.title("Hint 2")
answer = st.text_input(label="Antwoord op de puzzel", placeholder='...')
if str(answer).lower() in st.secrets['hint2']:
    st.write("The second number is ", st.secrets['sol2'])
st.image("hints/hint2.jpeg")

