import streamlit as st

up_file = st.camera_input(label="Take image")

if up_file is not None:
    st.session_state.up_file=up_file
    st.switch_page("pages/page_3.py")
st.page_link(label="Back",page="pages/page_1.py")