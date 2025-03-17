import streamlit as st

st.set_page_config(page_title="Sistem Pakar Kulit Wajah", layout="wide")

st.title("👩‍⚕️ Sistem Pakar Diagnosis Penyakit Kulit Wajah")

st.write(
    """
    Selamat datang di sistem pakar untuk mendiagnosis penyakit kulit wajah.
    Gunakan sistem ini untuk mengetahui kemungkinan penyakit kulit yang Anda alami 
    dan mendapatkan rekomendasi perawatan skincare yang sesuai.
    """
)

st.subheader("🔍 Mulai Diagnosis")
if st.button("🩺 Diagnosa Sekarang"):
    st.switch_page("pages/home.py")
