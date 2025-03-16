import streamlit as st
from auth.authentication import login, logout
from config.session_state import initialize_session
from pages.home import show_home_page
from pages.dashboard import show_dashboard

def main():
    initialize_session()
    
    if 'user' not in st.session_state:
        st.session_state.user = None
        
    if st.session_state.user:
        if st.sidebar.button("Logout"):
            logout()
        if st.session_state.user['role'] == 'admin':
            show_dashboard()
        else:
            show_home_page()
    else:
        st.title("Login Sistem Pakar Dermatologi")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if login(username, password):
                st.success("Login berhasil!")
                st.experimental_rerun()
            else:
                st.error("Username/password salah")

if __name__ == "__main__":
    main()