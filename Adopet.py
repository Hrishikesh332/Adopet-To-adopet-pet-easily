import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px
from plotly import graph_objects as go
from plotly.subplots import make_subplots
from streamlit_folium import folium_static
import folium
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import seaborn as sns

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
    
