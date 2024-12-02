import streamlit as st
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from PIL import Image,ImageDraw
import json
from gtts import gTTS
from io import BytesIO


load_dotenv()

API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

sys_prompt = """Consider yurself as personal assistant of a visually challenged person.
                Help them to read the textual content in the image provided.
                """

llm = genai.GenerativeModel(model_name='gemini-1.5-flash',system_instruction=sys_prompt)
prompt = 'Please extract texts from image provided in readable format. donot include special characters'
'''
st.title('Application to help visually challenged people')

img = st.file_uploader('Upload an Image',type=['png','jpeg','jpg'])
if img is not None:
    st.image(img)
    image = Image.open(img)

    prompt = 'Please extract texts from image provided in readable format. donot include special characters'

    response = llm.generate_content([image,prompt])
    st.write(response.text)
    response_text = response.text
    
language = st.selectbox('select language',['en','hi'])

if st.button('Generate Speech'):
    if response_text:
        tts = gTTS(response_text,lang=language)
        
        audio_stream = BytesIO()
        
        tts.write_to_fp(audio_stream)
        
        st.audio(audio_stream)
        
    else:
        st.warning('Please enter some text')
'''  
def text_extraction(img):
    image = Image.open(img)
    response = llm.generate_content([image,prompt])
    response_text = response.text
    st.write(response.text)
    language = st.selectbox('select language',['en','hi'])

    if st.button('Generate Speech'):
        if response_text:
            tts = gTTS(response_text,lang=language)
            
            audio_stream = BytesIO()
            
            tts.write_to_fp(audio_stream)
            st.audio(audio_stream)
        else:
            st.warning('Please enter some text')
