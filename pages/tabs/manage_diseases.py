import streamlit as st
import json
from models.database import get_all, get_by_id, get_all_symptoms

def show():
    st.header("Kelola Penyakit")
    
    # Ambil semua gejala untuk pilihan
    symptoms = get_all('symptoms')
    symptom_options = {s['id']: s['name'] for s in symptoms}

    # Form tambah penyakit
    with st.form("disease_form"):
        name = st.text_input("Nama Penyakit")
        description = st.text_area("Deskripsi")
        skincare = st.text_area("Rekomendasi Skincare")
        image_path = st.text_input("Path Gambar Penyakit")
        
        # Pilih gejala wajib
        st.subheader("Gejala Wajib")
        required = st.multiselect(
            "Pilih gejala wajib",
            options=symptom_options.values(),
            format_func=lambda x: symptom_options[x]
        )
        
        # Atur bobot gejala
        st.subheader("Bobot Gejala")
        weighted = {}
        for symptom in symptoms:
            weight = st.slider(
                f"Bobot untuk {symptom['name']}",
                0.0, 1.0, 0.0,
                key=f"weight_{symptom['id']}"
            )
            if weight > 0:
                weighted[str(symptom['id'])] = weight

        if st.form_submit_button("Simpan Penyakit"):
            try:
                new_disease = (
                    name,
                    json.dumps([s for s in required]),
                    json.dumps(weighted),
                    description,
                    skincare,
                    image_path
                )
                add_disease(new_disease)
                st.success("Penyakit berhasil ditambahkan!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    # Tampilkan data
    st.subheader("Daftar Penyakit")
    diseases = get_all('diseases')
    st.json(diseases)