import streamlit as st
from models.database import get_all
from models.logic import forward_chaining
from utils.styles import load_custom_css

def show_home_page():
    load_custom_css()
    st.title("Diagnosa Penyakit Kulit Wajah")
    
    # Ambil gejala dari database
    symptoms = get_all('symptoms')
    
    # Tampilkan gejala dalam bentuk grid
    selected = []
    cols = st.columns(3)
    
    for idx, symptom in enumerate(symptoms):
        with cols[idx % 3]:
            with st.container(border=True):
                if symptom['image_path']:
                    st.image(symptom['image_path'], width=150)
                if st.checkbox(symptom['name'], key=symptom['id']):
                    selected.append(symptom['id'])
    
    if st.button("Mulai Diagnosa"):
        if len(selected) < 1:
            st.warning("Pilih minimal 1 gejala")
        else:
            results = forward_chaining(selected)
            if results:
                show_result(results[0])
            else:
                st.error("Tidak ditemukan penyakit yang sesuai")

def show_result(result):
    disease = result['disease']
    with st.container(border=True):
        st.subheader(f"Hasil Diagnosa: {disease['name']}")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            if disease['disease_image']:
                st.image(disease['disease_image'], width=200)
        
        with col2:
            st.markdown(f"**Deskripsi:** {disease['description']}")
            st.markdown(f"**Rekomendasi Skincare:** {disease['skincare_recommendation']}")