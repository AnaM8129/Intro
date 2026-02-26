import streamlit as st
st.title("Mi primera app")
st.header("Esta es mi página de presentación")
from PIL import Image
image = Image.open("tarot.jpg")
st.image(image, caption="Esta es una imagen del tarot")
texto = st.text_input("Ingresa texto", "Texto inicial")
st.write("El texto que has escrito es", texto)
