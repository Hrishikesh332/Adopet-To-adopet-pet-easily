import streamlit as st
import pandas as pd
import os
from streamlit_folium import folium_static
import folium
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import pymongo
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

if (selected=="Pet"):
    
    #client = pymongo.MongoClient("mongodb+srv://m001-student:<m001-student>@sandbox.rn94l.mongodb.net/?retryWrites=true&w=majority")
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.Adopet


    with st.form("my_form"):
        st.write("Register the Pet:")


        animal=st.selectbox("Animal Type: ", df.Animal.unique().tolist())
        breed=st.selectbox("Breed Type: ", df.Type.unique().tolist())
        age1= st.selectbox("Age: ", df.Age.unique().tolist())
        gender=st.selectbox("Gender: ", df.Gender.unique().tolist())
        size=st.selectbox("Size: ", df.Size.unique().tolist())
        fur_type=st.selectbox("Fur: ", df.Fur.unique().tolist())
        color1=st.selectbox("Color of Fur: ", df.Color.unique().tolist())
        trained=st.selectbox("Training Status: ", df.Trained.unique().tolist())
        vaccinated=st.multiselect("Vaccination Status: ", df.Vaccinated.unique().tolist())
        l1=[]
        picture = st.camera_input("Take a picture")
        l1.append(picture)
        lang=st.text_input("Longitude", "")
        lati=st.text_input("Langitude", "")
        data= [ {'Animal': animal, 'Type':breed, "Age": age1, "Gender": gender, "Size": size, "Fur":fur_type, "Color":color1, "Trained": trained, "Vaccinated": vaccinated, "Image":l1, "Latitude": lati, "Longitude": lang}]
        st.write(data)
        submitted = st.form_submit_button("Submit")
        
    with client:

        db = client.Adopet
        db.Adopet.insert_many(data)


if (selected=="About us"):
    st.write("Made by Team: Four Bits")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('Dev Yadav')
        


    with col2:
        st.markdown("Hrishikesh Yadav")
        st.image("hrishi.jpeg")

    with col3:
        st.markdown("Shaloo singh")

    
    


        
