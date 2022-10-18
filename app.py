import streamlit as st
import pandas as pd
import os
from streamlit_folium import folium_static
import folium
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from pymongo import MongoClient

df=pd.read_csv('petd.csv')
try:
    import folium as f
except Exception:
    import folium as f

selected = option_menu(
            menu_title=None,  
            options=["Pet", "Find", "About us", "Sign/Signup"],  
            icons=["geo-alt", "pin-map", "bar-chart", "info-circle"],  
            menu_icon="cast",  
            default_index=0,  
            orientation="horizontal",
        )
if (selected=="About Us"):
    st.write("Adopet")
if (selected=="Pet"):
    
    client = MongoClient('mongodb://localhost:27017/')



    animal=st.selectbox("Animal Type: ", df.Animal.unique().tolist())
    breed=st.selectbox("Breed Type: ", df.Type.unique().tolist())
    age1= st.selectbox("Age: ", df.Age.unique().tolist())
    gender=st.selectbox("Gender: ", df.Gender.unique().tolist())
    size=st.selectbox("Size: ", df.Size.unique().tolist())
    fur_type=st.selectbox("Fur: ", df.Fur.unique().tolist())
    color1=st.selectbox("Color of Fur: ", df.Color.unique().tolist())
    trained=st.selectbox("Training Status: ", df.Trained.unique().tolist())
    vaccinated=st.multiselect("Vaccination Status: ", df.Vaccinated.unique().tolist())
    picture = st.camera_input("Take a picture")
    lang=st.text_input("Longitude", "")
    lati=st.text_input("Langitude", "")
        with client:

        db = client.Adopet
        data= [ {'Animal': animal, 'Type':breed, "Age": age1, "Gender": gender, "Size": size, "Fur":fur_type, "Color":color1, "Trained": trained, "Vaccinated": vaccinated, "Image
":picture, "Latitude": lati, "Longitude": lang}]
        db.data.insert(data)
        
