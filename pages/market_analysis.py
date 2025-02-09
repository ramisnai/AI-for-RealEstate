import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('data/real_estate_data.csv')

# Initialize session state variables
if 'theme' not in st.session_state:
    st.session_state.theme = "light"  # Default theme

def market_analysis_page():
    st.header("Market Analysis")
    
    # Price distribution chart
    st.subheader("Price Distribution")
    fig = px.histogram(data, x="price", nbins=30, title="Price Distribution")
    fig.update_layout(template="plotly_dark" if st.session_state.theme == "dark" else "plotly")
    st.plotly_chart(fig, use_container_width=True)
    
    # Average price by location
    st.subheader("Average Price by Location")
    avg_price_by_location = data.groupby('location')['price'].mean().sort_values(ascending=False)
    st.bar_chart(avg_price_by_location)