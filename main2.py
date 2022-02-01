import streamlit as st
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

st.markdown("'<h1 style='text-align:center;color:teal;'>Get Active User Details</h1>",unsafe_allow_html=True)
a=st.text_input("Enter the name of city","Type here....")
if st.button("CHECK"):
    geoloactor = Nominatim(user_agent="Ayush Arya")

    l = geoloactor.geocode(a)
    # print(l.latitude,l.longitude)
    df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [l.latitude,l.longitude], columns=['lat', 'lon'])
    st.map(df, zoom=None)
