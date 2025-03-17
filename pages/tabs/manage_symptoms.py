import streamlit as st
from models.setup_database import get_all, add_symptom
from utils.helpers import validate_input

def show():
    st.header("Kelola Gejala")
    
    # Form tambah gejala
    with st.form("symptom_form"):
        name = st.text_input("Nama Gejala")
        desc = st.text_area("Deskripsi")
        image = st.text_input("Path Gambar (contoh: /assets/symptoms/redness.jpg)")
        
        if st.form_submit_button("Tambah Gejala"):
            try:
                validate_input(name)
                add_symptom(name, desc, image)
                st.success("Gejala berhasil ditambahkan!")
            except Exception as e:
                st.error(str(e))
    
    # Tabel gejala
    symptoms = get_all('symptoms')
    st.dataframe(symptoms)