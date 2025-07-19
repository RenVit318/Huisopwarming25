import streamlit as st

if str(st.session_state.first_pass).lower() != st.secrets['first_pass']:
    st.write('Wat doe je hier?? Ga terug naar de hoofdpagina!!')
    st.stop()
    
st.title("Hint 3")
answer = st.text_input(label="Antwoord op de puzzel", placeholder='...')
if str(answer).lower() == st.secrets['hint3']:
    st.write("The third number is ", st.secrets['sol3'])
st.image("hints/hint3.jpeg")

