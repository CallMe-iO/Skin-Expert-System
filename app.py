import streamlit as st
from config.session_state import init_session
from auth.authentication import logout

init_session()

if st.session_state["authenticated"]:
    st.sidebar.write(f"👤 **{st.session_state['user']['username']}** ({st.session_state['user']['role']})")
    if st.sidebar.button("Logout"):
        logout()
        st.experimental_rerun()
else:
    st.warning("Silakan login terlebih dahulu!")
    st.stop()
