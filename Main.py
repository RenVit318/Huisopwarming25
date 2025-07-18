import streamlit as st
from PIL import Image
import os
import zipfile
import io
from datetime import datetime
import time


# Page configuration
st.set_page_config(
    page_title="Huisopwarming Rens",
    page_icon="🔥",
    layout="wide"
)

# Create uploads directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("Huisopwarming Rens 2025")
st.write("Let op: Als je dit tabblad sluit of opnieuw laad verdwijnt je voortgang.")

st.session_state.first_pass = st.text_input(label="Wachtwoord", placeholder="Dit heb je al kunnen zien..")

if st.session_state.first_pass != st.secrets['first_pass']:
    st.stop()

st.divider()

st.write("Welkom in het super geheime deel van deze website, je hebt met succes de eerste hint opgelost.")
st.write("In totaal zijn er vier hints verspreid door het huis. Gebruik de pagina's links om ze te vinden. Met allemaal samen kan je de kluis te kraken:")

st.session_state.kluis = st.text_input(label="De kluis", placeholder="Laatste linie voor grote geheimen..")

st.divider()

st.header("De andere spelers")
st.write("Upload hier een foto van jezelf als je mee doet aan de treasure hunt. (Ze worden achteraf gedownload en mogelijk veranderd in stickers.)")

# Upload section
uploaded_files = st.file_uploader(
    "Upload photos", 
    type=['png', 'jpg', 'jpeg'],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.rerun()

# Gallery
if os.path.exists(UPLOAD_DIR):
    photos = [f for f in os.listdir(UPLOAD_DIR) 
             if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if photos:
        cols = st.columns(3)
        for i, photo in enumerate(photos):
            with cols[i % 3]:
                img_path = os.path.join(UPLOAD_DIR, photo)
                image = Image.open(img_path)
                st.image(image, use_column_width=True)

# Hidden admin section
password = st.text_input(label="xxx", placeholder="Enter password for admin", type="password")

if password == st.secrets["admin_pass"]:
    if os.path.exists(UPLOAD_DIR):
        photos = [f for f in os.listdir(UPLOAD_DIR) 
                 if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        if photos:
            def create_zip():
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    for photo in photos:
                        photo_path = os.path.join(UPLOAD_DIR, photo)
                        zip_file.write(photo_path, photo)
                zip_buffer.seek(0)
                return zip_buffer.getvalue()
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            zip_data = create_zip()
            
            st.download_button(
                label="Download All Photos",
                data=zip_data,
                file_name=f"photos_{timestamp}.zip",
                mime="application/zip"
            )
            
            # Delete all photos button
            if st.button("🗑️ Delete All Photos", type="secondary"):
                for photo in photos:
                    photo_path = os.path.join(UPLOAD_DIR, photo)
                    os.remove(photo_path)
                st.success("All photos deleted!")
                st.rerun()
