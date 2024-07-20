import os

import requests
import streamlit as st
import os

st.set_page_config(layout="wide")

apiKey= os.environ['NASA_API']

url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}"

response = requests.get(url).json()
st.title(response['title'])
st.image(response['url'])
st.write(response['explanation'])






