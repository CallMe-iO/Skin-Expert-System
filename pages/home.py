import streamlit as st
from models.logic import forward_chaining, forward_chaining_weighted
from models.database import get_symptoms  # Ambil daftar gejala dari database

st.title("Sistem Pakar Diagnosis Penyakit Kulit Wajah")

# Membuat dua tab untuk metode FC dan FC berbobot
tab1, tab2 = st.tabs(["🔎 Diagnosa IF-THEN", "⚖️ Diagnosa dengan Bobot"])

# Ambil daftar gejala dari database (id dan nama)
symptoms_dict = get_symptoms()  # { "1": "Kulit kemerahan", "2": "Gatal", ... }
symptom_names = list(symptoms_dict.values())  # Hanya ambil nama gejala

# Tab 1: Diagnosa dengan Aturan IF-THEN
with tab1:
    st.subheader("Diagnosa Menggunakan Forward Chaining (IF-THEN)")
    selected_symptoms = st.multiselect("Pilih Gejala yang Anda Alami:", symptom_names, key="fc_ifthen")

    if st.button("Diagnosa - IF THEN"):
        # Konversi nama gejala yang dipilih menjadi ID
        selected_ids = [k for k, v in symptoms_dict.items() if v in selected_symptoms]
        
        diagnosis = forward_chaining(selected_ids)
        if diagnosis:
            st.success(f"✅ Hasil Diagnosa: **{diagnosis['penyakit']}**")
            st.write(f"📝 Penjelasan: {diagnosis['deskripsi']}")
            st.write(f"💡 Rekomendasi Skincare: {', '.join(diagnosis['skincare'])}")
        else:
            st.warning("❌ Tidak ada penyakit yang cocok dengan gejala yang dipilih.")

# Tab 2: Diagnosa dengan Bobot
with tab2:
    st.subheader("Diagnosa Menggunakan Forward Chaining dengan Bobot")
    selected_symptoms_weighted = st.multiselect("Pilih Gejala yang Anda Alami:", symptom_names, key="fc_bobot")

    if st.button("Diagnosa - Bobot"):
        # Konversi nama gejala yang dipilih menjadi ID
        selected_ids_weighted = [k for k, v in symptoms_dict.items() if v in selected_symptoms_weighted]

        diagnosis = forward_chaining_weighted(selected_ids_weighted)
        if diagnosis:
            st.success(f"✅ Hasil Diagnosa: **{diagnosis['penyakit']}** (Skor: {diagnosis['skor']:.2f})")
            st.write(f"📝 Penjelasan: {diagnosis['deskripsi']}")
            st.write(f"💡 Rekomendasi Skincare: {', '.join(diagnosis['skincare'])}")
        else:
            st.warning("❌ Tidak ada penyakit yang cocok dengan gejala yang dipilih.")
        