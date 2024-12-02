import streamlit as st
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from PIL import Image,ImageDraw


load_dotenv()

API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

sys_prompt = """Consider yurself as personal assistant of a visually challenged person.
                Help them to see what's around them by describing surrounding based on the image provided.
                Donot include unnecessary stuff just mention things that are important for a person to understand
                what's around them"""

llm = genai.GenerativeModel(model_name='gemini-1.5-flash',system_instruction=sys_prompt)
'''
st.title('Application to help visually challenged people')

img = st.file_uploader('Upload an Image',type=['png','jpeg','jpg'])
if img is not None:
    st.image(img)
    image = Image.open(img)

    prompt = 'Please describe the image provided to a visually challenged person'

    response = llm.generate_content([image,prompt])
    st.write(response.text)
'''
prompt = 'Please describe the image provided to a visually challenged person' 
def description(img):
    image = Image.open(img)
    response = llm.generate_content([image,prompt])
    return st.write(response.text)