import streamlit as st
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from PIL import Image,ImageDraw
import json
from gtts import gTTS
from io import BytesIO
from app import description
from newapp import text_extraction

st.title('VisionAI')
st.subheader("(An Application to help visually challenged person)")

img = st.file_uploader('Upload an Image',type=['png','jpeg','jpg'])
operation = st.sidebar.radio(
        'Select the operation you want to perform',
        ["Image Description","Text Extraction(Audio)"],
        captions=["It will describe the image so that visually challenged person can uderstand what's in the image",
                  "Extract text in the image and provide option to convert text to audio"]
    )
if img is not None:
    st.image(img)

   

    if operation=="Image Description":
        
        description(img)
    else:
        text_extraction(img)