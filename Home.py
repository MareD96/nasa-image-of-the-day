import requests
import streamlit as st
import os

st.set_page_config(layout="wide")

apiKey= os.environ['NASA_API']

url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}"

response = requests.get(url).json()
title = response['title']
image_url = response['url']
descirption = response['explanation']

image_filepath = "img.png"
requrest2 = requests.get(image_url)
with open(image_filepath,"wb") as file:
    file.write(requrest2.content)

st.title(title)
st.image(image_filepath)
st.write(descirption)





