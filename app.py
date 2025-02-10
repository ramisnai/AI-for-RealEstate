import streamlit as st
from pages.valuation import property_valuation_page
from pages.market_analysis import market_analysis_page
from pages.geospatial import geospatial_page

# Set page configuration
st.set_page_config(
    page_title="Real Estate Investing Tool",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables
if 'theme' not in st.session_state:
    st.session_state.theme = "light"  # Default theme

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Property Valuation", "Market Analysis", "Geospatial Analysis"])

# # Theme Toggle
# def toggle_theme():
#     if st.session_state.theme == "light":
#         st.session_state.theme = "dark"
#     else:
#         st.session_state.theme = "light"

# st.sidebar.button("Toggle Theme", on_click=toggle_theme)

# Apply theme
if st.session_state.theme == "dark":
    st.markdown('<style>body {background-color: #121212; color: white;}</style>', unsafe_allow_html=True)
else:
    st.markdown('<style>body {background-color: #f4f4f9; color: black;}</style>', unsafe_allow_html=True)


# Load the selected page
if page == "Home":
    st.title("Welcome to the Real Estate Investing Tool")
    st.write("""
    This tool helps you predict property prices, analyze market trends, and visualize property locations on a map.
    Use the sidebar to navigate between different features.
    """)
elif page == "Property Valuation":
    property_valuation_page()
elif page == "Market Analysis":
    market_analysis_page()
elif page == "Geospatial Analysis":
    geospatial_page()