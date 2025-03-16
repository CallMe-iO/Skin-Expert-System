import sqlite3
import bcrypt
import streamlit as st

# Fungsi untuk hash password
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# Fungsi untuk verifikasi password
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

# Fungsi untuk login user
def login_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, username, password, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    
    if user and verify_password(password, user[2]):  # Verifikasi password
        return {"id": user[0], "username": user[1], "role": user[3]}
    return None

# Fungsi untuk logout
def logout():
    st.session_state["authenticated"] = False
    st.session_state["user"] = None
