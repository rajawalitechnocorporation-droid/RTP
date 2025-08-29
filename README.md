# 📷 Aplikasi Upload Foto ke Google Drive (Streamlit + Service Account)

Aplikasi sederhana menggunakan **Streamlit** untuk mengupload foto dan langsung menyimpannya ke **Google Drive** menggunakan **Service Account**.

## 🚀 Cara Menjalankan di Lokal

1. Clone repository atau download zip ini.
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
3. Tambahkan file `service_account.json` (dari Google Cloud Console).
4. Edit `app.py`, ganti `FOLDER_ID` dengan ID folder Google Drive tujuan.
5. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

## 📂 Struktur Folder
```
foto-gdrive-app/
 ┣ 📄 app.py
 ┣ 📄 requirements.txt
 ┣ 📄 README.md
 ┗ 📄 service_account.json   (jangan upload ke GitHub publik!)
```

## 🌐 Deploy ke Streamlit Cloud

1. Upload project ini ke GitHub (tanpa `service_account.json`).
2. Di [Streamlit Cloud](https://share.streamlit.io/), buka **Settings > Secrets**.
3. Tambahkan isi `service_account.json` sebagai secret, contoh:
   ```toml
   SERVICE_ACCOUNT = '''
   { ... isi json service account ... }
   '''
   ```
4. Di `app.py`, ubah kode agar membaca dari secret Streamlit, bukan file lokal.
5. Deploy, aplikasi siap online.

---

✨ Dibuat dengan Python + Streamlit + Google Drive API.
