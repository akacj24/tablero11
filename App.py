import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title('Reconocimiento de Dígitos escritos a mano')

with st.sidebar:
  stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
  
drawing_mode = st.selectbox(
    "Select the drawing mode",
    ("freedraw", "Home phone", "Mobile phone"),
)

st.write("You selected:", drawing_mode)

stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", stroke_color)
bg_color = st.color_picker("Pick A Background Color", "#00f900")
st.write("The current Backgroundcolor is", bg_color)


# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=200,
    width=200,
    key="canvas",
)
