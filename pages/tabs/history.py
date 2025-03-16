import streamlit as st
from models.database import get_all
from utils.helpers import format_timestamp

def show():
    st.header("Riwayat Diagnosa")
    
    # Hanya admin yang bisa lihat semua riwayat
    if st.session_state.user['role'] == 'admin':
        history = get_all('history')
    else:
        history = get_history_by_user(st.session_state.user['id'])
    
    for entry in history:
        with st.expander(f"Diagnosa #{entry['id']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                **Tanggal**: {format_timestamp(entry['timestamp'])}  
                **Gejala Terpilih**: {len(json.loads(entry['symptoms']))} gejala
                """)
            with col2:
                st.markdown(f"""
                **Penyakit**: {entry['disease_id']}  
                **Probabilitas**: {entry['probability']}%
                """)
            if st.button("Detail", key=f"detail_{entry['id']}"):
                show_diagnosis_details(entry)

def show_diagnosis_details(entry):
    # Implementasi tampilan detail diagnosa
    pass