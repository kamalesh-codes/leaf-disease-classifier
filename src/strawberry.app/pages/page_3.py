import streamlit as st
import time
from PIL import Image
import requests

endpoint_url="http://localhost:8000/predict"

st.set_page_config(layout="wide")

def generate_stream(content:str):
    for char in content:
        time.sleep(0.003)
        yield char

def predict(file):
        response = requests.post(url=endpoint_url,files={"file":file.getvalue()})
        return response.json()

file_class_map={"healthy":"disease-treatments/healthy.txt",
                "angular_leafspot":"disease-treatments/angularleafspot.txt",
                "Calciumdeficiency":"disease-treatments/calciumdeficency.txt",
                "leaf_spot":"disease-treatments/leafspot.txt",
                "Leaf_scorch":"disease-treatments/leafscorch.txt"}

map={"healthy":"Healthy",
                "angular_leafspot":"Angular leafspot",
                "Calciumdeficiency":"Calcium deficiency",
                "leaf_spot":"Leaf spot",
                "Leaf_scorch":"Leaf scorch"}

c=st.columns([0.25,0.75],gap='small')
with c[0]:
    with st.container(key='image_container'):
        img = Image.open(st.session_state.up_file)
        response = predict(st.session_state.up_file)

        st.image(img,caption="Uploaded Image",width='content')
    st.header("Predicted class:",anchor=False)
    st.subheader(f"{map[response["predicted_class"]]}",anchor=False)
    st.subheader("Confidence Score:")
    st.subheader(f"{response["pred_prob"]}%")
    st.page_link(label="🏠 Home",page="pages/page_1.py")
                  
with c[1]:
    with open(file_class_map[response["predicted_class"]],"r") as file:
        content = file.readlines()
        for line in content:
            st.write_stream(generate_stream(line),cursor='>')