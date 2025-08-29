import streamlit as st
from PIL import Image

st.title("📸 Upload Foto Sederhana")

uploaded_file = st.file_uploader("Pilih file gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Foto yang diupload", use_column_width=True)
    st.success("✅ Foto berhasil diupload!")
