import torch

# import pandas as pd
# from pandas.io.formats.style import Styler

from PIL import Image
img = Image.open("pic1.jpg")
img.thumbnail((60,60))

from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import requests
import jinja2
import os

import sys
sys.path.append('/path/to/jinja2')

# for UI we install streamlit
import streamlit as st 

# Create round mask for image
import numpy as np
mask = Image.new('L', img.size, 0)
mask_np = np.array(mask)
y, x = np.ogrid[:img.size[1], :img.size[0]]
center = (int(img.size[0]/2), int(img.size[1]/2))
mask_np[(x - center[0])**2 + (y - center[1])**2 <= center[0]**2] = 255
mask = Image.fromarray(mask_np)
img.putalpha(mask)

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# img2txt
def img2txt(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(url)[0]["generated_text"]
    print(text)
    return text

# llm
def generate_story(scenario):
    generator = pipeline('text-generation', model='gpt2')
    story = generator(scenario, max_length=30, num_return_sequences=3)[0]["generated_text"]
    print(story)
    return story

# text to speech
def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payloads = {
        "inputs": message
    }

    response = requests.post(API_URL, headers=headers, json=payloads)
    with open('audio.mp3', 'wb') as file:
        file.write(response.content)

scenario = img2txt("sai1.jpg")
story = generate_story(scenario)
text2speech(story)

def main():
    st.set_page_config(page_title="image 2 audio story", page_icon="🚀")

    col1, col2 = st.columns([1, 3])
    
    col1.image(img, width=60, caption='MVNSP')
    st.header("PIC-TALK😀")
    st.header("Turns image🌆 into audio🔉 story✨")
    uploaded_file = st.file_uploader("Choose an image..", type="jpg")

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption="Uploaded Image.👍, Wait to be suprised🤗", use_column_width=True)
        scenario = img2txt(uploaded_file.name)
        story = generate_story(scenario)
        text2speech(story)

        with st.expander("scenario"):
            st.write(scenario)
        with st.expander("story"):
            st.write(story)

        st.audio("audio.mp3")

if __name__ == "__main__":
    main()

