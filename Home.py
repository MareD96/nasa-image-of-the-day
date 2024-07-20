import requests
import streamlit as st
import os

st.set_page_config(layout="wide")

apiKey= os.environ['NASA_API']

url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}"

image_path = "img.png"
response = requests.get(url).json()
title = response['title']
image_url = response['url']
description = response['explanation']

response2 = requests.get(image_url)
with open(image_path,"wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_path)
st.write(description)

