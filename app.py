import streamlit as st
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pydrive2.auth import ServiceAccountCredentials
from PIL import Image
import tempfile
import datetime
import os
import json

# --- Load Service Account dari Secrets ---
service_account_info = json.loads(st.secrets["SERVICE_ACCOUNT"])
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def connect_drive():
    gauth = GoogleAuth()
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        service_account_info, SCOPES
    )
    return GoogleDrive(gauth)

drive = connect_drive()

st.set_page_config(page_title="Upload Foto ke Google Drive", page_icon="📷", layout="wide")
st.title("📷 Upload Foto & Simpan ke Google Drive (Service Account)")

# Ganti dengan ID folder Google Drive kamu
FOLDER_ID = "PASTE_FOLDER_ID_KAMU_DI_SINI"

# --- Upload Foto ---
uploaded_file = st.file_uploader("Pilih foto untuk diupload", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Foto yang diupload", use_container_width=True)

    # Simpan sementara
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.getbuffer())
        tmp_path = tmp.name

    # Upload ke Google Drive
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    gfile = drive.CreateFile({
        'title': f"{timestamp}_{uploaded_file.name}",
        'parents': [{'id': FOLDER_ID}]
    })
    gfile.SetContentFile(tmp_path)
    gfile.Upload()

    st.success("✅ Foto berhasil disimpan ke Google Drive")
    st.write("🔗 Link File:", gfile['alternateLink'])
