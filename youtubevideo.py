import streamlit as st
import numpy as np
import cv2
from PIL import Image,ImageEnhance
st.title("Photo Converter")
#image=Image.open('ayushlogo.png')
#col1,col2=st.columns([0.8,0.2])
#with col1:
#    st.markdown("""<style> font{font-size:35px; font-family:'Cooper Black';color:#FF9633;<style>""",unsafe_allow_html=True)
#with col2:
#    st.image(image,width=150)

st.sidebar.markdown('<h1 class="font">Photo Converter</h1>',unsafe_allow_html=True)
with st.sidebar.expander("About the app"):
    st.write("""Use this simple app to convert your favorite photo to pencil sketch,a grayscale image\n@kabir arya """)
uploade=st.file_uploader("",type=['png','jpg','jpeg'])
if uploade is not None:
    image=Image.open(uploade)
    col1,col2=st.columns([0.5,0.5])
    with col1:
        st.markdown('<p style="text-align:center;">Before</p>',unsafe_allow_html=True)
        st.image(image,width=300)
    with col2:
        st.markdown('<p style="text-align:center">After</p>',unsafe_allow_html=True)
        filter=st.sidebar.radio('Convert Your Photo to :',['original','Night Effect','Gray Image','Pencil Sketch','Blur Effect','Thermal Effect[1]','Thermal Effect[2]','Love Effect','Ayush'])
        if filter =='Gray Image':
            converted_img=np.array(image.convert('RGB'))
            gray_scale=cv2.cvtColor(converted_img,cv2.COLOR_RGB2GRAY)
            st.image(gray_scale,width=300)
        elif filter=='Pencil Sketch':
            converted_img=np.array(image.convert('RGB'))
            gray_Scale=cv2.cvtColor(converted_img,cv2.COLOR_RGB2GRAY)
            inv_gray=255-gray_Scale
            slider=st.sidebar.slider("Adjust the intensity",25,255,125,step=2)
            bluer_image=cv2.GaussianBlur(inv_gray,(slider,slider),0,0)
            sketch=cv2.divide(gray_Scale,255-bluer_image,scale=256)
            st.image(sketch,width=300)
        elif filter=='Blur Effect':
            converted=np.array(image.convert('RGB'))
            slider=st.sidebar.slider('Adjust the intensity',5,81,33,step=2)
            converted=cv2.cvtColor(converted,cv2.COLOR_RGB2BGR)
            blur=cv2.GaussianBlur(converted,(slider,slider),0,0)
            st.image(blur,channels='BGR',width=300)
        elif filter=='Thermal Effect[1]':
            converted_img = np.array(image.convert('RGB'))
            gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2HSV)
            st.image(gray_scale, width=300)
        elif filter=='Thermal Effect[2]':
            converted_img = np.array(image.convert('RGB'))
            gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2HLS)
            st.image(gray_scale, width=300)
        elif filter=='Love Effect':
            converted_img = np.array(image.convert('RGB'))
            gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2LUV)
            st.image(gray_scale, width=300)
        elif filter=='Night Effect':
            converted_img = np.array(image.convert('RGB'))
            gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
            st.image(gray_scale, width=300)
        elif filter=='Ayush':
            converted_img = np.array(image.convert('RGB'))
            gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2LUV)
            st.image(gray_scale, width=300)

        else:
            st.image(image,width=300)
        st.sidebar.title('')
        st.sidebar.markdown('')
        st.sidebar.subheader('Please help us to improve!')
        with st.sidebar.form(key='columns_in_form', clear_on_submit=True):
            rating = st.slider("Please rate the app", min_value=1, max_value=5, value=3,
                               help='Drag the slider tp rate the app')
            text = st.text_input(label='Please leave your feedback here')
            submitted = st.form_submit_button('Submit')
            if submitted:
                st.write('Thanks for your feedback')
                st.markdown('Your Rating')
                st.markdown('Your Feedback')
                st.markdown(text)


