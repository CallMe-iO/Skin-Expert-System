import streamlit as st
from models.database import get_db_connection

def login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    
    if user:
        st.session_state.user = {
            "id": user[0],
            "username": user[1],
            "role": user[3]
        }
        return True
    return False

def logout():
    st.session_state.clear()