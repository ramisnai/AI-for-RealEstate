import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

# Load the dataset
data = pd.read_csv('data/real_estate_data.csv')

def plot_properties_on_map(data):
    avg_lat = data['latitude'].mean()
    avg_lon = data['longitude'].mean()
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=12)
    
    for idx, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Price: ${row['price']:,}",
            icon=folium.Icon(color="blue")
        ).add_to(m)
    
    return m

def geospatial_page():
    st.header("Geospatial Analysis")
    
    if 'latitude' in data.columns and 'longitude' in data.columns:
        map_plot = plot_properties_on_map(data)
        folium_static(map_plot)
    else:
        st.warning("Latitude and Longitude data not available.")