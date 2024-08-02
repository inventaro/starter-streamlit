from collections import namedtuple
import math
import pandas as pd
import streamlit as st
import openai
import os
import base64
from io import BytesIO

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

st.title("UI Elements")

"https://cheat-sheet.streamlit.app/"


@lambda f : f()
def sidebar():
    a = st.sidebar.radio('Choose:',[1,2])

@lambda f : f()
def make_photo():
    uploaded_file: BytesIO = st.camera_input("make a photo")
    if uploaded_file:
        st.toast('Nice Smile')
        st.image(uploaded_file)

        # save file
        with open(f"./static/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # download file and toast
        downloaded = st.download_button('download', uploaded_file, file_name=uploaded_file.name)
        if downloaded:
            st.toast('Thanks for downloading')

@lambda f : f()
def upload_file():
    uploaded_file: BytesIO = st.file_uploader('File uploader')
    if uploaded_file:
        uploaded_file
        with open(f"./static/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())

@lambda f : f()
def download_file():
    with open('./static/8PR56070NF932484U.pdf', 'rb') as f:
        st.download_button('Download PDF', f, file_name='file.pdf')


