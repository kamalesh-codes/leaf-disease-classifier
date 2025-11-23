import streamlit as st

if 'up_file' not in st.session_state:
    st.session_state.up_file = None 
    
st.set_page_config(layout='centered')
with st.container(vertical_alignment='center'):
    st.markdown("<h1 style='text-align: center;'>🍓Strawberry plant leaf-disease classifier</h1>",unsafe_allow_html=True)
    

with st.container():
    c=st.columns(2,gap='small')
    with c[0]:
        st.html("<h1 style='text-align: center;'>Upload Image</h1>")
        up_file = st.file_uploader(label="**Upload image**",label_visibility='hidden',type=['jpeg','jpg','png'],accept_multiple_files=False)
        if up_file is not None:
            st.session_state.up_file = up_file
            st.switch_page("pages/page_3.py")
    with c[1]:
        st.html("<h1 style='text-align: center;'>Take Image</h1>")
        with st.container():
            with st.container():
                pass
        cen = st.columns(3)
        with cen[1]:
            if st.button(label="Take image",width=200):
                st.switch_page("pages/page_2.py")



