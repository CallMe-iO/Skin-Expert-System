import streamlit as st
from models.database import get_all, add_symptom, add_disease
from pages.tabs import manage_symptoms, manage_diseases, manage_skincare, history

def show_dashboard():
    st.title("Dashboard Admin")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "Kelola Gejala", 
        "Kelola Penyakit", 
        "Kelola Skincare", 
        "Riwayat Diagnosa"
    ])
    
    with tab1:
        manage_symptoms.show()
    
    with tab2:
        manage_diseases.show()
    
    with tab3:
        manage_skincare.show()
    
    with tab4:
        history.show()