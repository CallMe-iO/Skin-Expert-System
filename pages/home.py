import streamlit as st
import sqlite3
import json
from models.logic import diagnose

st.title("Sistem Pakar Diagnosis Kulit Wajah")

# Ambil data gejala dari database
def get_symptoms():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM symptoms")
    symptoms = cursor.fetchall()
    conn.close()
    return symptoms

symptoms = get_symptoms()

# Form pilihan gejala
st.write("**Pilih Gejala yang Anda Alami:**")
selected_symptoms = st.multiselect(
    "Gejala:",
    options=[s[0] for s in symptoms],
    format_func=lambda x: dict(symptoms)[x]
)

# Tombol diagnosa
if st.button("Diagnosa Sekarang"):
    if selected_symptoms:
        result = diagnose(selected_symptoms)
        if result:
            disease_name, score, skincare = result[0]
            st.success(f"**Hasil Diagnosa: {disease_name}**")
            st.write(f"Skor Kecocokan: {score:.2f}")
            st.write("Rekomendasi Skincare:")
            for product in skincare:
                st.write(f"- {product}")
        else:
            st.warning("Tidak ada penyakit yang cocok dengan gejala yang dipilih.")
    else:
        st.error("Pilih setidaknya satu gejala.")
