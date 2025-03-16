import streamlit as st
import sqlite3
import json

st.title("📜 Riwayat Diagnosa")

# Ambil user_id dari session (pastikan user login)
user_id = st.session_state.user["id"] if "user" in st.session_state and st.session_state.user else None

if user_id is None:
    st.warning("Silakan login untuk melihat riwayat diagnosa.")
    st.stop()

# Fungsi menyimpan riwayat diagnosa
def save_diagnosis(user_id, selected_symptoms, disease, score, skincare):
    if user_id is None:
        return False  # Pastikan user login sebelum menyimpan

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history (user_id, symptoms, disease, score, skincare) 
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, json.dumps(selected_symptoms), disease, score, json.dumps(skincare)))

    conn.commit()
    conn.close()
    return True


# Ambil riwayat dari database
def get_history(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT symptoms, disease, score, skincare, timestamp 
        FROM history 
        WHERE user_id = ? 
        ORDER BY timestamp DESC
    """, (user_id,))
    
    history = cursor.fetchall()
    conn.close()
    return history

history_data = get_history(user_id)

if history_data:
    for symptoms, disease, score, skincare, timestamp in history_data:
        st.write(f"🕒 **{timestamp}**")
        st.write(f"🩺 **Diagnosis:** {disease}")
        st.write(f"📊 **Skor:** {score:.2f}")
        st.write(f"🔍 **Gejala yang Dipilih:** {', '.join(json.loads(symptoms))}")
        st.write(f"💊 **Rekomendasi Skincare:** {', '.join(json.loads(skincare))}")
        st.markdown("---")
else:
    st.info("Belum ada riwayat diagnosa.")
