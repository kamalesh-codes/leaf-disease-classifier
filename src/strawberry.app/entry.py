import streamlit as st

st.set_page_config(layout="centered")
pg=st.navigation([st.Page("pages/page_1.py",icon=":material/add_circle:"),\
                  st.Page("pages/page_2.py",icon=":material/create:"),
                  st.Page("pages/page_3.py")])
st.set_page_config(page_title="Strawberry leaf disease classification",page_icon=None)
pg.run()
