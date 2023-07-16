import streamlit as st
import numpy as np
import cv2

st.set_page_config(layout="wide",page_title="Image to Sketch Converter")
st.title("Image to Sketch Converter")

def image_to_sketch(image):

    gray_img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert=cv2.bitwise_not(gray_img)
    blur=cv2.GaussianBlur(invert, (21,21),0)
    inverted_blur=cv2.bitwise_not(blur)
    sketch=cv2.divide(gray_img, inverted_blur, scale=256.0)
    
    cv2.imwrite("Sketch.png",sketch)

img=st.file_uploader("Upload an image",type=['jpeg','png','jpg','jfif'])

if img is not None:
    image=np.frombuffer(img.getvalue(),dtype=np.uint8)
    image=cv2.imdecode(image,cv2.IMREAD_COLOR)
    convert=st.button("Convert")
    if convert:
        image_to_sketch(image)
        col1,col2=st.columns(2)
        with col1:
            st.image(img,caption="Original Image")
        with col2:
            st.image("Sketch.png",caption="Sketch")

            with open("Sketch.png","rb") as file:
                btn_id=st.download_button(
                    label="Download Sketch",
                    data=file,
                    file_name="Sketch.png",
                    mime="image/png"
                )
