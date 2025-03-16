import streamlit as st

if st.session_state["user"]["role"] != "admin":
    st.error("Akses ditolak! Halaman ini hanya untuk admin.")
    st.stop()

st.title("Dashboard Admin")
st.write("Selamat datang di halaman admin! 🚀")
